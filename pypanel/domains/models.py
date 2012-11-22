from django.db import models
from django.utils.translation import ugettext_lazy as _

import settings


class Domain(models.Model):
    user = models.ForeignKey('auth.User')
    name = models.CharField(max_length=250, unique=True)

    # DNS
    master = models.CharField(max_length=128, blank=True, null=True)
    last_check = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=6)
    notified_serial = models.IntegerField(blank=True, null=True)
    account = models.CharField(max_length=40, blank=True, null=True)

    # Mail
    transport = models.CharField(max_length=50, default='dovecot')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(db_index=True, default=True)

    class Meta(object):
        verbose_name = _('Domain')
        verbose_name_plural = _('Domains')

    def __unicode__(self):
        self.domain


class Records(models.Model):
    TYPES_OF_RECORDS = (
        ('SOA', 'SOA'),
        ('NS', 'NS'),
        ('MX', 'MX'),
        ('TXT', 'TXT'),
        ('PTR', 'PTR'),
        ('A', 'A'),
        ('AAAA', 'AAAA'),
        ('CNAME', 'CNAME'),
    )
    
    domain = models.ForeignKey(Domain, blank=True, null=True)
    name = models.CharField(max_length=255,  blank=True, null=True)
    type = models.CharField(choices=TYPES_OF_RECORDS, max_length=10, blank=True, null=True)
    content = models.CharField(max_length=65535, blank=True, null=True)
    ttl = models.IntegerField(blank=True, null=True)
    prio = models.IntegerField(blank=True, null=True)
    change_date = models.IntegerField(blank=True, null=True)
    # This is for add support for dns sec. But not now.
    #ordername = models.CharField(max_length=255)
    #auth = models.BooleanField()
    
    class Meta:
        verbose_name = _('Record')
        verbose_name_plural = _('Records')
    
    def __unicode__(self):
        return self.name


class Supermasters(models.Model):
    ip = models.IPAddressField()
    nameserver = models.CharField(max_length=255)
    account = models.CharField(max_length=40)

    def __unicode__(self):
        return self.nameserver
