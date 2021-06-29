from src.tasks.api import list_tasks, unique_id


def test_unique_id(tasks_db, task_mult_per_owner):
    existing_tasks = list_tasks()

    uid = unique_id()
    for t in existing_tasks:
        assert uid != t.id