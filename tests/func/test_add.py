import pytest
from bson import ObjectId

from src.tasks.api import Task, add, start_task_db, stop_tasks_db, get


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):  # tempdir - lokalziacja tymczasowa
    start_task_db(str(tmpdir), 'mongo')
    yield # yield jest po teardown
    stop_tasks_db()


def test_add_return_valid_id():
    new_task = Task('do something')
    t = add(new_task)
    assert isinstance(t, ObjectId)


def test_added_task_has_id_set():
    new_task = Task('learn python', owner='me', done=True)
    task_id = add(new_task)

    task_from_db = get(task_id)
    assert task_from_db.id == task_id