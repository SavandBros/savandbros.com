from fabric.operations import local


def manage_local(cmd):
    """
    Run manage.py on local.
    """
    local(f'python manage.py {cmd}')
