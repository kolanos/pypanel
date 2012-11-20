from django.conf import settings
from django.utils.translation import ugettext_lazy as _

ugettext = lambda s: s

IPV4 = 'IPv4'
IPV6 = 'IPv6'
IP_TYPE_CHOICES = ((IPV4, _('IPv4')),
                   (IPV6, _('IPv6')),)
IP_TYPE_DEFAULT = IPV4
