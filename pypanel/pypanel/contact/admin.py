from django.contrib import admin
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _

from .models import (BillingContact, TechnicalContact, AdministrativeContact,
                     Email, Phone, Contact, Country)


class BillingContactInline(admin.StackedInline):
    model = BillingContact
    fk_name = 'contact'
    max_num = 1


class TechnicalContactInline(admin.StackedInline):
    model = TechnicalContact
    fk_name = 'contact'
    max_num = 1


class AdministrativeContactInline(admin.StackedInline):
    model = AdministrativeContact
    fk_name = 'contact'
    max_num = 1


class EmailInline(admin.TabularInline):
    model = Email
    extra = 1


class PhoneInline(admin.TabularInline):
    model = Phone
    extra = 1


def user_link(self):
    url = reverse('admin:auth_user_change', args=[self.user.pk])
    return '<a href="%(url)s"><b>%(user)s</b></a>' % \
            {'url': url, 'user': self.user}
user_link.short_description = _('User')
user_link.admin_order_field = 'user'
user_link.allow_tags = True


def full_address(self):
    address = [x for x in [self.address, self.address2, self.city, self.state,
                           self.zip_code, self.country.iso3]
                           if x]
    return ', '.join(address)
full_address.short_description = _('Address')
full_address.admin_order_field = 'address'


class ContactAdmin(admin.ModelAdmin):
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
