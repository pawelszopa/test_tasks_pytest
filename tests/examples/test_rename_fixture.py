import pytest


@pytest.fixture(name='answer')
def ultimate_answer_to_life_the_universe_and_everything():
    return 42


def test_everything(answer):
    assert answer == 42
