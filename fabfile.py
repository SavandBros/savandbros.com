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
LANGUAGES = ('en', 'fa', )

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
            run('python manage.py collectstatic --noinput')
            run('chmod 644 tmp/restart.txt')

    run(f'selectorctl --interpreter python '
        f'--restart-webapp python_apps/{APP_NAME}')

    local('rm latest.zip')


def make_msgs():
    """Make translation messages."""
    for lang in LANGUAGES:
        local(f'django-admin.py makemessages -e json,html,py -l {lang} '
              f'--no-location --no-obsolete')


def compile_msgs():
    """Compile translation files."""
    local('django-admin.py compilemessages')


def clean_po_files() -> None:
    """Clean PO files and remove stuff we don't need."""
    po_files = []
    excludes = [
        'POT-Creation-Date',
        # 'PO-Revision-Date',
    ]

    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.po'):
                po_files.append(os.path.join(root, file))

    for file in po_files:
        clean = []

        with open(file, 'r') as file_handler:
            lines = file_handler.readlines()

            for line in lines:
                if all([i not in line for i in excludes]):
                    clean.append(line)

        with open(file, 'w') as file_handler:
            file_handler.writelines(clean)
