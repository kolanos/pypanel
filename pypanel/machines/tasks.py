from celery.task import task
from fabric.api import env, execute, local, run, sudo


def set_env_for_machine(machine):
    if machine.is_remote:
        env.hosts = [machine.hostname]
        env.user = machine.user
        env.password = machine.password


# Machine Tasks


@task(name='Create Machine')
def create_machine(machine):
    pass


# IP Tasks

@task(name='Add IP Address')
def add_ip_address(ip):
    pass


@task(name='Remove IP Address')
def remove_ip_address(ip):
    pass


# System User Tasks


@task(name='Create System User')
def create_system_user(user):
    set_env_for_machine(user.machine)

    def command(username):
        if env.is_remote:
            if env.user == 'root':
                run('adduser %s' % username)
            else:
                sudo('adduser %s' % username)
        else:
            local('adduser %s' % username)

    execute(command, username=user.username)


@task(name='Change System User')
def change_system_user(system_user):
    pass


@task(name='Delete System User')
def delete_system_user(user):
    set_env_for_machine(user.machine)

    def command(username):
        if env.is_remote:
            if env.user == 'root':
                run('deluser %s' % username)
            else:
                sudo('deluser %s' % username)
        else:
            local('deluser %s' % username)

    execute(command, username=user.username)


@task(name='Enable System User')
def enable_system_user(system_user):
    pass


@task(name='Disable System User')
def disable_system_user(system_user):
    pass


# System Group Tasks


@task(name='Create System Group')
def create_group(system_group):
    pass


@task(name='Delete System Group')
def delete_system_group(system_group):
    pass
