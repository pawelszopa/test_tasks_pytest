import pytest

from src.tasks.api import unique_id, start_task_db, stop_tasks_db


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):  # tempdir - lokalziacja tymczasowa
    start_task_db(str(tmpdir), 'mongo')
    yield  # yield jest po teardown
    stop_tasks_db()


def test_unique_id():
    id_1 = unique_id()
    id_2 = unique_id()
    assert id_1 != id_2
