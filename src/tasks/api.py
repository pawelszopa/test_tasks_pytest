from collections import namedtuple

from bson import ObjectId

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)


class TaskException(Exception):
    """A tasks error has occurred"""


class UninitializedDatabase(TaskException):
    """ Call tasks.start tasks db() before other function"""


def add(task):
    if not isinstance(task, Task):
        raise TypeError('task must be Task object')
    if not isinstance(task.summary, str):
        raise ValueError('task.summary must be string')
    if not ((task.owner is None) or isinstance(task.owner, str)):
        raise ValueError('task.owner must be string or None')
    if task.id is not None:
        raise ValueError('task.id must be None')
    if _tasksdb is None:
        raise UninitializedDatabase()

    task_id = _tasksdb.add(task._asdict())

    return task_id


def get(task_id):
    if not isinstance(task_id, ObjectId):
        raise TypeError('task id must be an ObjectId')
    if _tasksdb is None:
        raise UninitializedDatabase()

    task_dict = _tasksdb.get(task_id)
    task_dict['id'] = task_dict['_id']
    del task_dict['_id']
    return Task(**task_dict)


def list_tasks(owner=None):
    if owner and not isinstance(owner, str):
        raise TypeError('owner must be a string')
    if _tasksdb is None:
        raise UninitializedDatabase()

    return [Task(**t) for t in _tasksdb.list_tasks(owner)]


def count():
    if _tasksdb is None:
        raise UninitializedDatabase()

    return _tasksdb.count()


def update(task_id, task):
    if not isinstance(task_id, ObjectId):
        raise TypeError("there is not task with this task")
    if not isinstance(task, Task):
        raise TypeError('task must be Task object')

    current_task_db = _tasksdb.get(task_id)
    current_task = Task(**current_task_db)._asdict()
    updates = task._asdict()

    current_task |= updates
    _tasksdb.update(task_id, current_task)


def delete(task_id):
    if not isinstance(task_id, ObjectId):
        raise TypeError("there is not task with this task")
    if _tasksdb is None:
        raise UninitializedDatabase()

    _tasksdb.delete(task_id)


def delete_all():
    if _tasksdb is None:
        raise UninitializedDatabase()

    _tasksdb.delete_all()


def unique_id():
    if _tasksdb is None:
        raise UninitializedDatabase()

    return _tasksdb.unique_id()


_tasksdb = None


def start_task_db(db_path, db_type):
    if not isinstance(db_path, str):
        raise TypeError('db path must be a string')

    global _tasksdb

    if db_type == 'tiny':
        pass
    elif db_type == 'mongo':
        import src.tasks.tasksdb_pymongo as tasksdb_pymongo
        _tasksdb = tasksdb_pymongo.start_tasks_db(db_path)
    else:
        raise ValueError('db_type must be a tiny or mongo')


def stop_tasks_db():
    global _tasksdb
    if _tasksdb is not None:
        _tasksdb._stop_mongod()
        _tasksdb = None