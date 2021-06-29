import pytest
from bson import ObjectId

from src.tasks.api import Task, add, start_task_db, stop_tasks_db, get, count


def test_add_return_valid_id(tasks_db_session):
    new_task = Task('do something')
    t = add(new_task)
    assert isinstance(t, ObjectId)

@pytest.mark.smoke
def test_added_task_has_id_set(tasks_db_session):
    new_task = Task('learn python', owner='me', done=True)
    task_id = add(new_task)

    task_from_db = get(task_id)
    assert task_from_db.id == task_id


def test_add_increases_count(db_with_3_tasks):
    add(Task('Add new task'))
    assert count() == 4
