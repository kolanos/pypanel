from django.db import models
from django.utils.translation import ugettext_lazy as _

import settings


class Plan(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    bandwidth = models.BigIntegerField(_('Bandwidth'),
                                       default=settings.PLAN_BANDWIDTH_LIMIT_DEFAULT,
                                       help_text=_('In bytes, -1 is unlimited.'))
    disk = models.BigIntegerField(_('Disk Space'),
                                  default=settings.PLAN_DISK_LIMIT_DEFAULT,
                                  help_text=_('In bytes, -1 is unlimited.'))
    memory = models.BigIntegerField(_('Memory'),
                                    default=settings.PLAN_MEMORY_LIMIT_DEFAULT,
                                 help_text=_('In bytes. The soft memory '
                                             'limit for this user, '
                                             '-1 is unlimited.'))
    users = models.IntegerField(_('Users'),
                                  default=settings.PLAN_USER_LIMIT_DEFAULT,
                                  help_text=_('Number of system users, '
                                              '-1 is unlimited.'))
    domains = models.IntegerField(_('Domains'),
                                  default=settings.PLAN_DOMAIN_LIMIT_DEFAULT,
                                  help_text=_('Number of domains that can '
                                              'be hosted, -1 is unlimited.'))
    databases = models.IntegerField(_('Databases'),
                                    default=settings.PLAN_DATABASE_LIMIT_DEFAULT,
                                    help_text=_('Number of databases that can '
                                                'be hosted, -1 is unlimited.'))
    mailboxes = models.IntegerField(_('Mailboxes'),
                                    default=settings.PLAN_MAILBOX_LIMIT_DEFAULT,
                                    help_text=_('Number of mailboxes that can '
                                                'be hosted, -1 is unlimited.'))
    webapps = models.IntegerField(_('Web Apps'),
                                  default=settings.PLAN_WEBAPP_LIMIT_DEFAULT,
                                  help_text=_('Number of web apps that can '
                                              'be hosted, -1 is unlimited.'))
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('Plan')
        verbose_name_plural = _('Plans')

    def __unicode__(self):
        return self.name


class Term(models.Model):
    plan = models.ForeignKey(Plan)
    term = models.PositiveSmallIntegerField(choices=settings.PLAN_TERM_CHOICES,
                                             default=settings.PLAN_TERM_DEFAULT)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    setup = models.DecimalField(max_digits=12, decimal_places=2)
    active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('plan', 'term',)
        verbose_name = _('Plan Term')
        verbose_name_plural = _('Plan Terms')

    def __unicode__(self):
        return '%s %s' % (self.plan.name, self.term)
