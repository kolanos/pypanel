#!/usr/bin/env python

from fabric.api import *
from fabric.colors import white, red
from fabric.network import prompt_for_password

def main():
    """Installation main menu"""
    local('clear')
    print "Welcome to the %s installation!\n" % white("PyPanel", True)
    print "%s Ensure that your system is a clean install of %s before proceeding.\n" % (red("IMPORTANT:", True),
                                                                                        white("Ubuntu Server Edition 10.04", True))
    print white("Select from the options below:\n", True)
    print "1. Install PyPanel now"
    print "2. Exit installation\n"

    option = prompt("Enter an option:", default="2", validate=r"^[1-2]$")

    if option == '1':
        local('clear')
        install()
    elif option == '2':
        print "\nExiting..."
        exit()

def install():
    """Begin installation"""
    print white("\nBegin installation!\n", True)
    print "Before we begin, we need to know where you want to install PyPanel."
    print "You can either install remotely or locally."
    print "Either way we require root access in order to install."
    print "So if you don't have your root password, get it now."
    print "Also make sure that you can SSH into the remote/local host as root.\b"

    host = prompt("Enter server hostname or IP:", default="localhost")
    user = prompt("Enter root username:", default="root")
    password = prompt_for_password("Enter root password: ", True)

    env.user = user
    env.hosts = [host]

def ntpdate():
    """Create daily ntpdate cron job, run ntpdate for good measure."""
    file_write('/etc/cron.daily/ntpdate', 'ntpdate ntp.ubuntu.com', '755')
    run('ntpdate ntp.ubuntu.com')

if __name__ == "__main__":
    main()
