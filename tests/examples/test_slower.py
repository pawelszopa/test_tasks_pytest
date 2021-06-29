import pytest
from datetime import datetime
from random import random
import time


@pytest.fixture(autouse=True)
def check_duration(request, cache):
    key = 'duration/' + request.node.nodeid.replace(':', '_')

    start_time = datetime.now()
    yield
    stop_time = datetime.now()
    this_duration = (stop_time - start_time).total_seconds()
    last_duration = cache.get(key, None)
    cache.set(key, this_duration)
    if last_duration is not None:
        error_string = 'test duration over 2x last duration'
        assert this_duration <= last_duration * 2, error_string


@pytest.mark.parametrize('i', range(5))
def test_slow_staff(i):
    time.sleep(random())
