from doit.tools import LongRunning


def task_pytest():
    return {
        'actions': ['pytest'],
        'doc': 'runs tests with pytest'
    }


def task_lint():
    cmd = ['pylint --rcfile=setup.cfg **/*.py',
           'flake8',
           'bandit -r --ini setup.cfg']

    for c in cmd:
        yield {'name': c.split()[0],
               'actions': [LongRunning(c)]}
