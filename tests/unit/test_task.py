import pytest

from src.tasks.api import Task, update


@pytest.mark.get
@pytest.mark.smoke
def test_asdict():
    t_task = Task('do sth', 'igor', True, 21)
    t_dict = t_task._asdict()
    expected = {
        'summary': 'do sth',
        'owner': 'igor',
        'done': True,
        'id': 21
    }
    assert t_dict == expected


@pytest.mark.smoke
def test_default():
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2


def test_member_access():
    t = Task('buy car', 'igor')
    assert t.summary == 'buy car'
    assert t.owner == 'igor'
    assert (t.done, t.id) == (False, None)


def test_replace():
    t_before = Task('buy car', 'igor', False)
    t_after = t_before._replace(id=10, done=True)
    t_expected = Task('buy car', 'igor', True, 10)
    assert t_after == t_expected
