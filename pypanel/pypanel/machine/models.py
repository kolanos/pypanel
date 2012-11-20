from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from pypanel.machine import settings


class Machine(models.Model):
    hostname = models.CharField(max_length=255)
    db_server = models.BooleanField(_('DB Server'), default=False)
    dns_server = models.BooleanField(_('DNS Server'), default=False)
    ftp_server = models.BooleanField(_('FTP Server'), default=False)
    mail_server = models.BooleanField(_('Mail Server'), default=False)
    web_server = models.BooleanField(_('Web Server'), default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('Machine')
        verbose_name_plural = _('Machines')

    def __unicode__(self):
        return self.hostname


class IP(models.Model):
    machine = models.ForeignKey(Machine)
    user = models.ForeignKey(User, blank=True, null=True)
    ip_type = models.CharField(choices=settings.IP_TYPE_CHOICES,
                               default=settings.IP_TYPE_DEFAULT, max_length=4)
    ip_address = models.GenericIPAddressField()
    virtualhost = models.BooleanField(default=True)
    virtualhost_port = models.CharField(default='80,443', max_length=255)

    class Meta:
        verbose_name = _('IP Address')
        verbose_name_plural = _('IP Addresses')

    def __unicode__(self):
        return self.ip_address


class SSHUser(models.Model):
    machine = models.ForeignKey(Machine)
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    quota = models.BigIntegerField(default=-1)
    puser = models.CharField(max_length=255, null=True)
    pgroup = models.CharField(max_length=255, null=True)
    shell = models.CharField(max_length=255, null=True)
    homedir = models.CharField(max_length=255, null=True)
    chroot = models.CharField(max_length=255, null=True)
    ssh_rsa = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('SSH User')
        verbose_name_plural = _('SSH Users')

    def __unicode__(self):
        return self.username
