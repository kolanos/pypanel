from django.db import models
from django.utils.translation import ugettext_lazy as _


class Mailbox(models.Model):
    domain = models.ForeignKey('domain.Domain')
    username = models.CharField(db_index=True, max_length=255)
    password = models.CharField(max_length=255)
    name = models.CharField(blank='', max_length=255)
    maildir = models.CharField(max_length=255)
    quota = models.BigIntegerField(default=0)
    local_part = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    active = self.BooleanField(db_index=True, default=True)

    class Meta(object):
        unique_together = ('domain', 'username')
        verbose_name = _('Mailbox')
        verbose_name_plural = _('Mailboxes')

    def __unicode__(self):
        self.username


class Alias(models.Model):
    alias = models.CharField(max_length=255)
    domain = models.ForeignKey('domain.Domain', blank=True, null=True)
    mailbox = models.ForeignKey(Mailbox)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(db_index=True, default=True)

    class Meta(object):
        unique_together = ('alias', 'mailbox')
        verbose_name = _('Alias')
        verbose_name_plural = _('Aliases')

    def __unicode__(self):
        return self.address


class AliasDomain(models.Model):
    alias_domain = models.ForeignKey('domain.Domain')
    target_domain = models.ForeignKey('domain.Domain')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True, index=True)

    class Meta(object):
        unique_together = ('alias_domain', 'target_domain')
        verbose_name = _('Alias Domain')
        verbose_name_plural = _('Alias Domains')

    def __unicode__(self):
        return self.alias_domain



