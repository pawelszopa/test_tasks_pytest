import pytest

from src.tasks.api import Task, get, add, stop_tasks_db, start_task_db


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):  # tempdir - lokalziacja tymczasowa
    start_task_db(str(tmpdir), 'mongo')
    yield  # yield jest po teardown
    stop_tasks_db()


def equivalent(t1, t2):
    return (
            (t1.summary == t2.summary) and
            (t1.owner == t2.owner) and
            (t1.done == t2.done)
    )


def test_add_1():
    task = Task('learn python', 'igor', True)
    task_id = add(task)

    t_from_db = get(task_id=task_id)
    assert equivalent(task, t_from_db)


@pytest.mark.parametrize('task',
                         [
                             Task('sleep', done=False),
                             Task('wake', 'igor'),
                             Task('breath', 'IGOR', True),
                             Task('exercise', 'IGoR', False),
                         ]
                         )
def test_add2(task):
    task_id = add(task)
    t_from_db = get(task_id)
    assert equivalent(t_from_db, task)


@pytest.mark.parametrize('summary, owner, done',
                         [
                             ('sleep', None, False),
                             ('wake', 'igor', False),
                             ('breath', 'IGOR', True),
                             ('exercise', 'IGoR', False),
                         ]
                         )
def test_add3(summary, owner, done):
    task = Task(summary, owner, done)
    task_id = add(task)
    t_from_db = get(task_id)
    assert equivalent(t_from_db, task)


task_to_try = (
    Task('sleep', done=False),
    Task('wake', 'igor'),
    Task('breath', 'IGOR', True),
    Task('exercise', 'IGoR', False),
)


@pytest.mark.parametrize('task', task_to_try)
def test_add4(task):
    task_id = add(task)
    t_from_db = get(task_id)
    assert equivalent(t_from_db, task)


task_ids = [f'Task({t.summary, t.owner, t.done})' for t in task_to_try]
# id daja mozliwosc w raporatach do sprawedzenia danych bo jak damy -v to widzimy parametry (w fail tez bedzie dane zamiast task0)
@pytest.mark.parametrize('task', task_to_try, ids=task_ids)
def test_add5(task):
    task_id = add(task)
    t_from_db = get(task_id)
    assert equivalent(t_from_db, task)


@pytest.mark.parametrize('task',
                         [
                             pytest.param(Task('sleep', done=False), id='just summary'),
                             pytest.param(Task('wake', 'igor'), id='summary/owner'),
                             pytest.param(Task('breath', 'IGOR', True), id='summary/owner/done'),
                             pytest.param(Task('exercise', 'IGoR', False), id='summary/owner/done'),
                         ]
                         )
def test_add6(task):
    task_id = add(task)
    t_from_db = get(task_id)
    assert equivalent(t_from_db, task)


@pytest.mark.parametrize('task', task_to_try, ids=task_ids)
class TestAdd:
    def test_equivalent(self, task):
        task_id = add(task)
        t_from_db = get(task_id)
        assert equivalent(t_from_db, task)

    def test_valid_id(self, task):
        task_id = add(task)
        t_from_db = get(task_id)
        assert t_from_db.id == task_id