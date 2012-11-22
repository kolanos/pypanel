from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import Q

import settings


class Machine(models.Model):
    hostname = models.CharField(max_length=255)
    primary_ip = models.ForeignKey('machines.IP', blank=True, null=True,
                                   related_name='primary_ip',
                                   verbose_name=_('Primary IP'))
    is_remote = models.BooleanField(_('Is remote?'), default=True,
                                    help_text=_('If unchecked, commands for '
                                                'this machine will be run '
                                                'locally.'))
    username = models.CharField(default=settings.MACHINE_USER_DEFAULT,
                                max_length=32,
                                help_text=_('This should be either the root '
                                            'or sudo user used to execute '
                                            'commands.'))
    password = models.CharField(blank=True, max_length=255, null=True,
                                help_text=_("Either the root or sudo "
                                            "user's password."))

    # Services Available
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
    user = models.ForeignKey(User, blank=True, null=True,
                             verbose_name=_('Owner'),
                             help_text=_('Assign a dedicated IP address '
                                         'to a user. If left blank, the '
                                         'IP can be used by multiple users.'))
    ip_type = models.CharField(_('IP Type'), choices=settings.IP_TYPE_CHOICES,
                               default=settings.IP_TYPE_DEFAULT, max_length=4)
    ip_address = models.GenericIPAddressField(_('IP Address'))
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
    name = models.CharField(max_length=32)
    gid = models.PositiveIntegerField(_('GID'))
    users = models.ManyToManyField('SystemUser', blank=True,
                                   null=True)

    class Meta:
        unique_together = (('machine', 'name',), ('machine', 'gid',),)
        verbose_name = _('System Group')
        verbose_name_plural = _('System Groups')

    def __unicode__(self):
        return self.name


class SystemUser(models.Model):
    machine = models.ForeignKey(Machine)
    user = models.ForeignKey(User, blank=True, null=True,
                             verbose_name=_('Owner'))
    username = models.CharField(max_length=32)
    password = models.CharField(blank=True, max_length=255, null=True)
    uid = models.PositiveIntegerField(_('UID'))
    group = models.ForeignKey(SystemGroup, blank=True, null=True)
    shell = models.CharField(default=settings.USERS_DEFAULT_SHELL,
                             max_length=255)
    homedir = models.CharField(_('Base Home Directory'),
                               default=settings.USERS_DEFAULT_HOMEDIR,
                               max_length=255, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('machine', 'username'), ('machine', 'uid'),)
        verbose_name = _('System User')
        verbose_name_plural = _('System Users')

    def __unicode__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.uid:
            try:
                self.uid = User.objects(Q(machine=self.machine))\
                               .order_by('-uid')[0].uid + 1
            except IndexError:
                self.uid = settings.USERS_START_UID
        super(SystemUser, self).save(*args, **kwargs)
