import pytest
import json
from src.tasks.api import Task, start_task_db, stop_tasks_db, delete_all, add


# 2 bazy na raz
# @pytest.fixture(scope="session", params=('tiny', 'mongo'))
@pytest.fixture(scope="session", params=['mongo'])
def tasks_db_session(tmpdir_factory, request):
    temp_dir = tmpdir_factory.mktemp('temp')
    start_task_db(str(temp_dir), request.param)

    yield

    stop_tasks_db()


@pytest.fixture()
def tasks_db(tasks_db_session):
    delete_all()


@pytest.fixture(scope='session')
def tasks_just_a_few():
    """All summaries and owners are unique"""
    return (
        Task("Write some code", "Igor", True),
        Task("Code review Igor's code", "Katie", False),
        Task("Fix what Igor did", "Patrick", False),
    )


@pytest.fixture(scope='session')
def task_mult_per_owner():
    """Several owners with several tasks each. """
    return (
        Task("Write some code", "Igor", False),
        Task("Drink beer", "Igor", False),
        Task("Time for cocaine", "Igor", False),

        Task("Code", "Katie", False),
        Task("Code review Igor's code", "Katie", False),
        Task("Code review", "Katie", False),

        Task("Fix what Igor did", "Patrick", False),
        Task("Pizza time", "Patrick", False),
        Task("Netflix", "Patrick", False),
    )


@pytest.fixture()
def db_with_3_tasks(tasks_db, tasks_just_a_few):
    for t in tasks_just_a_few:
        add(t)


# Examples for different cases than the project
@pytest.fixture(scope='module')
def author_file_json(tmpdir_factory):
    python_author_data = {
        "Igor": {"City": "Krakow"},
        "Kate": {"City": "Breclav"},
        "Patrick": {"City": "Cracov"},
    }

    file_ = tmpdir_factory.mktemp('data').join("author_file.json")
    print(f'file: {str(file_)}')

    with file_.open('w') as f:
        json.dump(python_author_data, f)

    return file_
