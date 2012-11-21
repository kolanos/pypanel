from django.contrib import admin
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from .models import Machine, IP, SystemGroup, SystemUser


class IPInline(admin.TabularInline):
    model = IP
    extra = 1


class SystemGroupInline(admin.TabularInline):
    model = SystemGroup
    extra = 1


class MachineAdmin(admin.ModelAdmin):
    fieldsets = (
            (None, {'fields': (('hostname', 'active',),)}),
            (_('Services'), {'fields': ('db_server', 'dns_server',
                                        'ftp_server', 'mail_server',
                                        'web_server',)}),
        )
    inlines = [SystemGroupInline, IPInline]
    list_display = ('hostname', 'db_server', 'dns_server', 'ftp_server',
                    'mail_server', 'web_server', 'active',)
    list_display_links = ('hostname',)
    list_filter = ('db_server', 'dns_server', 'ftp_server', 'mail_server',
                   'web_server', 'active',)
    search_fields = ('hostname',)

    class Media:
        js = ['js/collapsed_stacked_inlines.js']


def machine_link(self):
    url = reverse('admin:machine_machine_change', args=[self.machine.pk])
    return '<a href="%(url)s"><b>%(machine)s</b></a>' % \
            {'url': url, 'machine': self.machine}
machine_link.short_description = _('Machine')
machine_link.admin_order_field = 'machine'
machine_link.allow_tags = True


class IPAdmin(admin.ModelAdmin):
    list_filter = ('ip_type', 'machine__hostname',)
    list_display = ('ip_address', 'ip_type', machine_link,)
    search_fields = ('ip_address',)


admin.site.register(Machine, MachineAdmin)
admin.site.register(IP, IPAdmin)
admin.site.register(SystemGroup)
admin.site.register(SystemUser)
