from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Plan, Term
from .utils import format_bytes


class TermInline(admin.TabularInline):
    model = Term
    extra = 1


def bandwidth(self):
    return format_bytes(self.bandwidth) \
            if self.bandwidth >= 0 else _('Unlimited')
bandwidth.short_description = _('Bandwidth')
bandwidth.admin_order_field = 'bandwidth'


def disk(self):
    return format_bytes(self.disk) \
            if self.disk >= 0 else _('Unlimited')
disk.short_description = _('Disk Space')
disk.admin_order_field = 'disk'


def memory(self):
    return format_bytes(self.memory) \
            if self.memory >= 0 else _('Unlimited')
memory.short_description = _('Memory')
memory.admin_order_field = 'memory'


class PlanAdmin(admin.ModelAdmin):
    fieldsets = (
            (None, {'fields': (('name', 'active',), 'description',)}),
            (_('Resource Limits'), {
                'fields': ('bandwidth', 'disk', 'memory', 'users', 'domains',
                           'databases', 'mailboxes', 'webapps')}),
        )
    inlines = [TermInline]
    list_display = ('name', bandwidth, disk, memory, 'active',)
    list_display_links = ('name',)
    list_filter = ('active',)
    search_fields = ('name',)

    class Media:
        js = ['js/collapsed_stacked_inlines.js']


admin.site.register(Plan, PlanAdmin)
