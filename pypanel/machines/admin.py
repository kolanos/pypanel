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
            (None, {'fields': (('hostname', 'active',),
                                'is_remote', 'primary_ip', 'username',
                                'password')}),
            (_('Services'), {'fields': (('db_server', 'dns_server',
                                        'ftp_server', 'mail_server',
                                        'web_server',),)}),
        )
    inlines = [SystemGroupInline, IPInline]
    list_display = ('hostname', 'db_server', 'dns_server', 'ftp_server',
                    'mail_server', 'web_server', 'active',)
    list_display_links = ('hostname',)
    list_filter = ('db_server', 'dns_server', 'ftp_server', 'mail_server',
                   'web_server', 'active',)
    search_fields = ('hostname',)


def machine_link(self):
    url = reverse('admin:machines_machine_change', args=[self.machine.pk])
    return '<a href="%(url)s"><b>%(machine)s</b></a>' % \
            {'url': url, 'machine': self.machine}
machine_link.short_description = _('Machine')
machine_link.admin_order_field = 'machine'
machine_link.allow_tags = True


class IPAdmin(admin.ModelAdmin):
    list_filter = ('ip_type', 'machine__hostname',)
    list_display = ('ip_address', 'ip_type', machine_link,)
    search_fields = ('ip_address',)


class SystemUserAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('machine', 'user', 'username', 'password',)}),
        (_('Additional Information'), {
            'classes': ('collapse',),
            'fields': ('uid', 'group', 'shell', 'homedir',)}),
        )
    list_filter = ('machine__hostname',)
    list_display = ('username', machine_link,)
    search_fields = ('username',)

    class Media:
        js = ['js/collapsed_stacked_inlines.js']


    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['machine']
        else: # This is an addition
            return []

admin.site.register(Machine, MachineAdmin)
admin.site.register(IP, IPAdmin)
admin.site.register(SystemGroup)
admin.site.register(SystemUser, SystemUserAdmin)
