from django.conf import settings
from django.utils.translation import ugettext_lazy as _

ugettext = lambda s: s

# Plan Limits
PLAN_BANDWIDTH_LIMIT_DEFAULT = getattr(settings, 'PLAN_BANDWIDTH_LIMIT', -1)
PLAN_DATABASE_LIMIT_DEFAULT = getattr(settings, 'PLAN_DATABASE_LIMIT', -1)
PLAN_DISK_LIMIT_DEFAULT = getattr(settings, 'PLAN_DISK_LIMIT', -1)
PLAN_DOMAIN_LIMIT_DEFAULT = getattr(settings, 'PLAN_DOMAIN_LIMIT', -1)
PLAN_MAILBOX_LIMIT_DEFAULT = getattr(settings, 'PLAN_MAILBOX_LIMIT', -1)
PLAN_MEMORY_LIMIT_DEFAULT = getattr(settings, 'PLAN_MEMORY_LIMIT', 268435456)
PLAN_USER_LIMIT_DEFAULT = getattr(settings, 'PLAN_USER_LIMIT', -1)
PLAN_WEBAPP_LIMIT_DEFAULT = getattr(settings, 'PLAN_WEBAPP_LIMIT', -1)

# Plan Terms
PLAN_TERM_MONTHLY = getattr(settings, 'PLAN_TERM_MONTHLY', 1)
PLAN_TERM_QUARTERLY = getattr(settings, 'PLAN_TERM_QUARTERLY', 3)
PLAN_TERM_BIANNUALLY = getattr(settings, 'PLAN_TERM_BIANNUALLY', 6)
PLAN_TERM_YEARLY = getattr(settings, 'PLAN_TERM_YEARLY', 12)
PLAN_TERM_CHOICES = getattr(settings, 'PLAN_TERM_CHOICES',
        ((PLAN_TERM_MONTHLY, _('Monthly')),
        (PLAN_TERM_QUARTERLY, _('Quarterly')),
        (PLAN_TERM_BIANNUALLY, _('Bi-Anually')),
        (PLAN_TERM_YEARLY, _('Yearly'))))
PLAN_TERM_DEFAULT = getattr(settings, 'PLAN_TERM_DEFAULT', PLAN_TERM_MONTHLY)
