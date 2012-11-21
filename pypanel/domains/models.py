from django.db import models
from django.utils.translation import ugettext_lazy as _

import settings


class Domain(models.Model):
    machine = models.ForeignKey('machines.Machine')
    domain = models.CharField(db_index=True, max_length=255)
    aliases = models.IntegerField(default=0)
    mailboxes = models.IntegerField(default=0)
    maxquota = models.BigIntegerField(default=0)
    quota = models.BigIntegerField(default=0)
    transport = models.CharField(choices=settings.TRANSPORT_OPTIONS,
                                 default=settings.TRANSPORT_DEFAULT,
                                 max_length=7)
    backupmx = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(db_index=True, default=True)

    class Meta(object):
        verbose_name = _('Domain')
        verbose_name_plural = _('Domains')

    def __unicode__(self):
        self.domain
