import pytest

from src.tasks.api import unique_id, start_task_db, stop_tasks_db, Task, add
import src.tasks as tasks


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):  # tempdir - lokalziacja tymczasowa
    start_task_db(str(tmpdir), 'mongo')
    yield  # yield jest po teardown
    stop_tasks_db()


@pytest.mark.xfail()  # X bedzie jesli pomimo xfail test przejdzie x bedzie jesli fail - ale test nei bedzie fail nigdy widadc to na -v
def test_unique_id():
    uuid = unique_id()
    assert uuid == 'a duck'


#     moze to sie przydac przy testowaniu  rzeczy ktore sa zalezne od jakiegos innego API np.


def test_unique_id_2():
    ids = []
    ids.append(add(Task('one')))
    ids.append(add(Task('two')))
    ids.append(add(Task('three')))

    uuid = unique_id()
    assert uuid not in ids

# jesli wersja jest za niska to spodziewwamy sie ze test zrobi fail
# dziala tylko wtedy kiedy jest true tasks.verion zwraca true

@pytest.mark.xfail(
    tasks.__version__ < '0.2.0', reason="not supported until version 0.2.0", )
def test_unique_id():
    id_1 = unique_id()
    id_2 = unique_id()
    assert id_1 != id_2
