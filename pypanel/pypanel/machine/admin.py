from django.contrib import admin
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _

from .models import Machine, IP


class IPInline(admin.TabularInline):
    model = IP
    extra = 1


class MachineAdmin(admin.ModelAdmin):
    fieldsets = (
            (None, {'fields': ('user', 'name',)}),
            ('Address', {'fields': ('address', 'address2', 'city', 'state',
                                    'zip_code', 'country')}),
        )
    inlines = [EmailInline, PhoneInline, BillingContactInline,
               TechnicalContactInline, AdministrativeContactInline]
    list_display = ('name', user_link, 'email', 'phone', full_address,)
    list_display_links = ('name',)
    search_fields = ['name', 'user__username', 'user__email', 'email__address',
                     'phone__number']

    class Media:
        js = ['js/collapsed_stacked_inlines.js']


class CountryAdmin(admin.ModelAdmin):
    list_display = ('printable_name',)
    search_fields = ('printable_name',),


admin.site.register(Contact, ContactAdmin)
admin.site.register(Country, CountryAdmin)
