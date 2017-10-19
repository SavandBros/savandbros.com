from contextlib import contextmanager

import os
from fabric.api import env
from fabric.context_managers import cd, prefix
from fabric.operations import run, local, put


REMOTE_USER = os.environ.get('REMOTE_USER')
APP_NAME = os.environ.get('APP_NAME')
APPS_PATH = f'/home/{REMOTE_USER}/python_apps'
APP_PATH = f'{APPS_PATH}/{APP_NAME}'
VENV_PATH = f'/home/{REMOTE_USER}/virtualenv/python__apps_{APP_NAME}/3.5'
VENV_ACTIVATE_PATH = f'source {VENV_PATH}/bin/activate'


env.user = REMOTE_USER
env.hosts = [os.environ.get('REMOTE_HOST'), ]
env.port = int(os.environ.get('REMOTE_PORT'))


@contextmanager
def venv():
    """Activate the virtualenv."""
    with cd(VENV_PATH):
        with prefix(VENV_ACTIVATE_PATH):
            yield


def deploy():
    """Deploying to production."""
    local('git archive HEAD --format=zip > latest.zip')
    put('latest.zip', APPS_PATH)

    with cd(APPS_PATH):
        run(f'rm -rf {APP_NAME}')
        run(f'unzip latest.zip -d {APP_NAME}')
        run('rm latest.zip')

    with venv():
        with cd(APP_PATH):
            run('pip install -r requirements.txt')
            run('python manage.py collectstatic')
            run('chmod 644 tmp/restart.txt')

    run(f'selectorctl --interpreter python '
        f'--restart-webapp python_apps/{APP_NAME}')

    local('rm latest.zip')
