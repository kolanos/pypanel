from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import Q

import settings


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

    @property
    def ips(self):
        return self.ip_set.count()


class IP(models.Model):
    machine = models.ForeignKey(Machine)
    user = models.ForeignKey(User, blank=True, null=True)
    ip_type = models.CharField(_('IP Type'), choices=settings.IP_TYPE_CHOICES,
                               default=settings.IP_TYPE_DEFAULT, max_length=4)
    ip_address = models.GenericIPAddressField(_('IP Address'), unpack_ipv4=True)
    virtualhost = models.BooleanField(_('VirtualHost'), default=True)
    virtualhost_port = models.CommaSeparatedIntegerField(_('VirtualHost Port'),
                                                         default='80,443',
                                                         max_length=255)

    class Meta:
        verbose_name = _('IP Address')
        verbose_name_plural = _('IP Addresses')

    def __unicode__(self):
        return self.ip_address


class SystemGroup(models.Model):
    machine = models.ForeignKey(Machine)
    name = models.CharField(max_length=30)
    gid = models.PositiveIntegerField()
    users = models.ManyToManyField('SystemUser', blank=True, null=True)

    class Meta:
        unique_together = (('machine', 'name',), ('machine', 'gid',),)
        verbose_name = _('System Group')
        verbose_name_plural = _('System Groups')

    def __unicode__(self):
        return self.name

 
class SystemUser(models.Model):
    machine = models.ForeignKey(Machine)
    user = models.ForeignKey(User, blank=True, null=True)
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    quota = models.BigIntegerField(default=-1,
                                   help_text=_('In bytes, -1 is unlimited.'))
    uid = models.PositiveIntegerField(_('UID'))
    group = models.ForeignKey(SystemGroup, default=settings.USERS_DEFAULT_GROUP_PK)
    shell = models.CharField(default=settings.USERS_DEFAULT_SHELL,
                             max_length=255)
    homedir = models.CharField(_('Home Directory'),
                               default=settings.USERS_DEFAULT_HOMEDIR,
                               max_length=255, null=True)
    chroot = models.CharField(max_length=255, null=True)
    ssh_rsa = models.TextField(_('SSH RSA'))
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('machine', 'username'), ('machine', 'uid'),)
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __unicode__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.uid:
            try:
                self.uid = User.objects(Q(machine=self.machine))\
                               .order_by('-uid')[0].uid + 1
            except IndexError:
                self.uid = settings.USERS_START_UID
        super(User, self).save(*args, **kwargs)       
