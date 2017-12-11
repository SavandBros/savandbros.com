from distutils.util import strtobool
from typing import Optional, List

import shutil
from fabric.operations import local, os

from fabfile import fab_config
from fabfile import fab_development

CONFIRM_POSITIVE = ['yes', 'y', 'yeah', ]
COVERAGE_REPORT_HTML_DIR = 'coverage_html'
COVERAGE_REPORT_FILE = '.coverage'


def get_apps_tests(app_name: Optional[str] = '',
                   exclude: Optional[str] = None) -> str:
    """
    Creating a app or test case name list.

    :param app_name: Application or test case name.
    :param exclude: Exclude an application from testing.
    """
    if app_name not in ['', None]:
        app_name = app_name.replace('/', '.').replace('.py', '')

    if exclude:
        apps = fab_config.apps
        apps.remove(exclude)

        return ' '.join(apps)

    return app_name


def get_test_command(app_name: Optional[str] = '',
                     keep_db: Optional[bool] = True,
                     parallel: Optional[bool] = True,
                     fake_migrations: Optional[bool] = True,
                     exclude: Optional[str] = None) -> str:
    """
    Creating the test command for ``manage.py``.

    :param app_name: App name to run the tests against
    :param keep_db: To keep the db and not destroy it.
        This will optimize the test time.
    :param parallel: To run the tests in parallel.
        This will optimize the test time.
    :param fake_migrations: Faking the migration instead of actually
        running them.
        This will optimize the test time.
    :param exclude: Exclude an application from testing.
    """
    base_command = 'test {0}'.format(get_apps_tests(app_name, exclude))
    args: List[str] = []

    if fake_migrations:
        os.environ.setdefault('DJANGO_FAKE_MIGRATIONS', 'YES')

    if keep_db:
        args.append('-k')

    if parallel:
        args.append('--parallel 6')

    return '{base_command} --noinput -v3 {args}'.format(
        base_command=base_command, args=' '.join(args)
    )


def coverage() -> None:
    """Code coverage report."""
    if os.path.exists(COVERAGE_REPORT_HTML_DIR):
        shutil.rmtree(COVERAGE_REPORT_HTML_DIR)

    if os.path.isfile(COVERAGE_REPORT_FILE):
        os.remove(COVERAGE_REPORT_FILE)

    local("coverage run --source='.' manage.py {0}".format(get_test_command(
        parallel=False, fake_migrations=False, keep_db=False
    )))

    local("coverage report --skip-covered")
    local("coverage html")


def test(app_name: Optional[str] = '', exclude: Optional[str] = None,
         parallel: Optional[str] = 'y', fake_db: Optional[str] = 'y',
         keep_db: Optional[str] = 'y') -> None:
    """Running the tests."""
    parallel = bool(strtobool(parallel))
    fake_db = bool(strtobool(fake_db))
    keep_db = bool(strtobool(keep_db))

    if not keep_db:
        fake_db = False

    fab_development.manage_local(
        get_test_command(
            app_name=app_name, keep_db=keep_db, parallel=parallel,
            fake_migrations=fake_db, exclude=exclude
        )
    )
