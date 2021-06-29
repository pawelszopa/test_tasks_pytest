import time

import pytest


# scope session zmienia na odpalenie sie przed wszystkim i po wszystkim czyuli tylko raz.
@pytest.fixture(autouse=True, scope='session')
def footer_session_scope():
    yield
    now = time.time()
    print('--')
    print(f'finished{time.strftime("%d %b %X", time.localtime(now))}')
    print('--' * 20)


@pytest.fixture(autouse=True)
def footer_function_scope():
    start = time.time()
    yield
    stop = time.time()
    delta = stop - start
    print(f'\nTest duration: {delta:0.3}')


def test_1():
    time.sleep(1)


def test_2():
    time.sleep(1.23)
