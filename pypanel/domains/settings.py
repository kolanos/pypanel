from django.conf import settings
from django.utils.translation import ugettext_lazy as _

ugettext = lambda s: s

# NOTE: Doesn't validate unicode characters
DOMAIN_REGEX = ('^([a-z0-9]([-a-z0-9]*[a-z0-9])?\\.)+((a[cdefgilmnoqrstuwxz]|'
                'aero|arpa)|(b[abdefghijmnorstvwyz]|biz)|(c[acdfghiklmnorsuvx'
                'yz]|cat|com|coop)|d[ejkmoz]|(e[ceghrstu]|edu)|f[ijkmor]|(g[a'
                'bdefghilmnpqrstuwy]|gov)|h[kmnrtu]|(i[delmnoqrst]|info|int)|'
                '(j[emop]|jobs)|k[eghimnprwyz]|l[abcikrstuvy]|(m[acdghklmnopq'
                'rstuvwxyz]|mil|mobi|museum)|(n[acefgilopruz]|name|net)|(om|o'
                'rg)|(p[aefghklmnrstwy]|pro)|qa|r[eouw]|s[abcdeghijklmnortvyz'
                ']|(t[cdfghjklmnoprtvwz]|travel)|u[agkmsyz]|v[aceginu]|w[fs]|'
                'y[etu]|z[amw])$')

# Domain Mail Transport
VIRTUAL_TRANSPORT = 'virtual'
LOCAL_TRANSPORT = 'local'
RELAY_TRANSPORT = 'relay'
TRANSPORT_OPTIONS = ((VIRTUAL_TRANSPORT, _("Virtual Account")),
                     (LOCAL_TRANSPORT, _("System Account")),
                     (RELAY_TRANSPORT, _("Backup MX Relay")),)
TRANSPORT_DEFAULT = VIRTUAL_TRANSPORT
