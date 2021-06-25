import pytest
from bson import ObjectId

from src.tasks.api import add, list_tasks, get, delete, start_task_db, update, Task


def test_add_raises():
    with pytest.raises(TypeError):
        add(Task='this is not a  task')


@pytest.mark.smoke
def test_list_tasks_raises():
    with pytest.raises(TypeError):
        list_tasks(owner=123)


@pytest.mark.get
@pytest.mark.smoke
def test_get_raises():
    with pytest.raises(TypeError):
        get(123)


class TestUpdate:
    @staticmethod
    def test_bad_id():
        with pytest.raises(TypeError):
            update(task_id={'dict instead': 1}, task=Task())

    @staticmethod
    def test_bad_object_type():
        with pytest.raises(TypeError):
            update(ObjectId(), {'dict': 'yeah'})


def test_delete_raises():
    with pytest.raises(TypeError):
        delete(task_id=321)


def test_start_task_db_raises():
    with pytest.raises(TypeError):
        start_task_db(2)
    with pytest.raises(ValueError) as exinfo:
        start_task_db('some/great/path', 'mysql')
    assert exinfo.value.args[0] == 'db_type must be a tiny or mongo'
    assert exinfo.type == ValueError
