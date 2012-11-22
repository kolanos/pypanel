from django.conf import settings
from django.utils.translation import ugettext_lazy as _

ugettext = lambda s: s

MACHINE_USER_DEFAULT = 'root'

IPV4 = getattr(settings, 'IPV4', 'ipv4')
IPV6 = getattr(settings, 'IPV6', 'ipv6')
IP_TYPE_CHOICES = getattr(settings, 'IP_TYPE_CHOICES',
        ((IPV4, _('IPv4')), (IPV6, _('IPv6'))))
IP_TYPE_DEFAULT = getattr(settings, 'IP_TYPE_DEFAULT', IPV4)

USERS_START_UID = getattr(settings, 'USERS_DEFAULT_START_UID', 1001)
USERS_DEFAULT_GROUP_PK = getattr(settings, 'USERS_DEFAULT_GROUP_PK', 1)
USERS_DEFAULT_HOMEDIR = getattr(settings, 'USERS_DEFAULT_BASE_HOMEDIR', '/home/')
USERS_DEFAULT_SHELL = getattr(settings, 'USERS_DEFAULT_SHELL', '/bin/false')
