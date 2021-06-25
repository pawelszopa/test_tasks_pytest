from src.tasks.api import Task


def test_task_equality():
    t = Task('buy car', 'igor')
    b = Task('buy beer', 'pawel')
    assert not t == b


def test_dict_equality():
    t_dict = Task('buy car', 'igor')._asdict()
    expected = Task('buy beer', 'pawel')._asdict()

    assert t_dict != expected
