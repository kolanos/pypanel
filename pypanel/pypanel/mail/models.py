from django.db import models
from django.utils.translation import ugettext_lazy as _


class Domain(models.Model):
    VIRTuaL_TRANSPORT = 'virtual'
    LOCAL_TRANSPORT = 'local'
    RELAY_TRANSPORT = 'relay'
    TRANSPORT_OPTIONS = ((VIRTUAL_TRANSPORT, _("Virtual Account")),
                         (LOCAL_TRANSPORT, _("System Account")),
                         (RELAY_TRANSPORT, _("Backup MX Relay")))

    domain = models.CharField(db_index=True, max_length=255)
    description = models.CharField(blank=True, max_length=255)
    aliases = models.IntegerField(default=0)
    mailboxes = models.IntegerField(default=0)
    maxquota = models.BigIntegerField(default=0)
    quota = models.BigIntegerField(default=0)
    transport = models.CharField(choies=TRANSPORT_OPTIONS, default='virtual',
                                 max_length=255)
    backupmx = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(db_index=True, default=True)

    class Meta(object):
        verbose_name = _('Domain')
        verbose_name_plural = _('Domains')

    def __unicode__(self):
        self.domain


class Mailbox(models.Model):
    domain = models.ForeignKey(Domain)
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
    mailbox = models.ForeignKey(Mailbox)
    domain = models.ForeignKey(Domain, blank=True, null=True)
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
    alias_domain = models.ForeignKey(Domain)
    target_domain = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True, index=True)

    class Meta(object):
        unique_together = ('alias_domain', 'target_domain')
        verbose_name = _('Alias Domain')
        verbose_name_plural = _('Alias Domains')

    def __unicode__(self):
        return self.alias_domain



