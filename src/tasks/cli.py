import contextlib
import os

import click
import api
from api import Task


@click.group(context_settings={'help_option_names': ['-h', '--help']})
@click.version_option(version='0.1.0')
def task_cli():
    """Run the tasks application"""


@task_cli.command()
@click.argument('summary')
@click.option('-o', '--owner', default=None, help='set the task owner')
def add(summary, owner):
    with _task_db():
        api.add(Task(summary, owner))


@contextlib.contextmanager
def _task_db():
    api.start_task_db(os.path.join('~', 'data', 'db'), 'mongo')
    yield
    api.stop_tasks_db()


@task_cli.command(help="add a task")
@click.argument('summary')
@click.option('-o', '--owner', default=None,
              help='set the task owner')
def add(summary, owner):
    """Add a task to db."""
    with _task_db():
        api.add(Task(summary, owner))


@task_cli.command(help="delete a task")
@click.argument('task_id', type=int)
def delete(task_id):
    """Remove task in db with given id."""
    with _task_db():
        api.delete(task_id)


@task_cli.command(name="list", help="list tasks")
@click.option('-o', '--owner', default=None,
              help='list tasks with this owner')
def list_tasks(owner):
    """
    List tasks in db.
    If owner given, only list tasks with that owner.
    """
    formatstr = "{: >4} {: >10} {: >5} {}"
    print(formatstr.format('ID', 'owner', 'done', 'summary'))
    print(formatstr.format('--', '-----', '----', '-------'))
    with _task_db():
        for t in api.list_tasks(owner):
            done = 'True' if t.done else 'False'
            owner = '' if t.owner is None else t.owner
            print(formatstr.format(
                t.id, owner, done, t.summary))


@task_cli.command(help="update task")
@click.argument('task_id', type=int)
@click.option('-o', '--owner', default=None,
              help='change the task owner')
@click.option('-s', '--summary', default=None,
              help='change the task summary')
@click.option('-d', '--done', default=None,
              type=bool,
              help='change the task done state (True or False)')
def update(task_id, owner, summary, done):
    """Modify a task in db with given id with new info."""
    with _task_db():
        api.update(task_id, Task(summary, owner, done))


@task_cli.command(help="list count")
def count():
    """Return number of tasks in db."""
    with _task_db():
        c = api.count()
        print(c)


if __name__ == '__main__':
    task_cli()
