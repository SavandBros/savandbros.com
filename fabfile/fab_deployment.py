"""Fabric is fabric friend."""
from contextlib import contextmanager

import os
from fabric.api import env
from fabric.context_managers import cd, prefix
from fabric.operations import run, local, put

REMOTE_USER = os.environ.get('REMOTE_USER')
LANGUAGES = ('en', 'fa', )
env.user = REMOTE_USER
env.hosts = [os.environ.get('REMOTE_HOST'), ]
env.port = int(os.environ.get('REMOTE_PORT'))


class AppConfig:
    """Application configuration."""

    def __init__(self):
        self.app_name = os.environ.get('APP_NAME')

    def get_app_name(self):
        return self.app_name

    def get_apps_path(self):
        return f'/home/{REMOTE_USER}/python_apps'

    def get_app_path(self):
        return f'{self.get_apps_path()}/{self.get_app_name()}'

    def get_venv_path(self):
        app_name = self.app_name
        return f'/home/{REMOTE_USER}/virtualenv/python__apps_{app_name}/3.6'

    def get_venv_activate_path(self):
        return f'source {self.get_venv_path()}/bin/activate'


app_cfg = AppConfig()


@contextmanager
def venv():
    """Activate the virtualenv."""
    with cd(app_cfg.get_venv_path()):
        with prefix(app_cfg.get_venv_activate_path()):
            yield


def set_staging():
    """Set the host target to staging machines."""
    app_cfg.app_name = os.environ.get('APP_NAME_STAGING')


def set_prod():
    """Set the host target to production machines."""
    app_cfg.app_name = os.environ.get('APP_NAME_PROD')


def deploy():
    """Deploying to production."""
    app_name = app_cfg.get_app_name()
    app_path = app_cfg.get_app_path()
    apps_name = app_cfg.get_apps_path()

    local('git archive HEAD --format=zip > latest.zip')
    put('latest.zip', apps_name)

    with cd(apps_name):
        run(f'rm -rf {app_name}')
        run(f'unzip latest.zip -d {app_name}')
        run('rm latest.zip')

    with venv():
        with cd(app_path):
            run('pip install -r requirements.txt')
            run('python manage.py collectstatic --noinput')
            run('python manage.py  migrate')
            run('chmod 644 tmp/restart.txt')

    run(f'selectorctl --interpreter python '
        f'--restart-webapp python_apps/{app_name}')

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
