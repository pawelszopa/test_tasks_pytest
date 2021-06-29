import pytest


@pytest.fixture(scope='function')
def func_scope():
    """Function scope fixture"""


@pytest.fixture(scope='module')
def mod_scope():
    """Module scope fixture"""


@pytest.fixture(scope='session')
def sess_scope():
    """Session scope fixture"""


@pytest.fixture(scope='class')
def class_scope():
    """Class scope fixture"""


def test_1(sess_scope, mod_scope, func_scope):
    """Test using session, module and function scope fixture"""


@pytest.mark.usefixtures('class_scope')
class TestSomething:

    def test_2(self):
        """Class scope fixture"""
