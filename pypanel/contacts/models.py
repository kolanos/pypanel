from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Country(models.Model):
    name = models.CharField(max_length=64)
    printable_name = models.CharField(max_length=64)
    iso = models.CharField(_('ISO'), max_length=2)
    iso3 = models.CharField(_('ISO3'), max_length=3, null=True)
    numcode = models.PositiveSmallIntegerField(null=True)

    def __unicode__(self):
        return self.printable_name

    class Meta(object):
        ordering = ('name',)
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')


class BaseContact(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    address = models.CharField(_('Address'), max_length=255)
    address2 = models.CharField(_('Address (cont.)'), max_length=255, blank=True)
    city = models.CharField(_('City'), max_length=20)
    state = models.CharField(_('State'), max_length=255)
    zip_code = models.CharField(_('Zip Code'), max_length=20)
    country = models.ForeignKey(Country, verbose_name=_('Country'))

    class Meta(object):
        abstract = True
        verbose_name = _('Contact')
        verbose_name_plural = _("Contacts")

    def __unicode__(self):
        return self.name


class Contact(BaseContact):
    user = models.OneToOneField(User)

    @property
    def phone(self):
        phone = Phone.objects.filter(contact=self, preferred=True)
        if not phone:
            phone = Phone.objects.filter(contact=self, preferred=False)
            if not phone:
                return ''
        return phone[0].number

    @property
    def email(self):
        email = Email.objects.filter(contact=self, preferred=True)
        if not email:
            email = Email.objects.filter(contact=self, preferred=False)
            if not email:
                return ''
        return email[0].address

    @property
    def billing(self):
        try:
            b = BillingContact.objects.get(contact=self)
        except BillingContact.DoesNotExist:
            return self
        else:
            return b

    @property
    def administrative(self):
        try:
            a = AdministrativeContact.objects.get(contact=self)
        except AdministrativeContact.DoesNotExist:
            return self
        else:
            return a

    @property
    def technical(self):
        try:
            t = TechnicalContact.objects.get(contact=self)
        except TechnicalContact.DoesNotExist:
            return self
        else:
            return t


class Email(models.Model):
    contact = models.ForeignKey(Contact)
    address = models.EmailField(_('Email Address'))
    preferred = models.BooleanField(_('Preferred Email'), default=False)

    class Meta(object):
        verbose_name = _('Email Address')
        verbose_name_plural = _('Email Addresses')

    def __unicode__(self):
        return self.address


class Phone(models.Model):
    contact = models.ForeignKey(Contact)
    number = models.CharField(_('Phone Number'), max_length=20)
    preferred = models.BooleanField(_('Preferred Number'), default=False)

    class Meta(object):
        verbose_name = _('Phone Number')
        verbose_name_plural = _('Phone Numbers')

    def __unicode__(self):
        return self.number


class BillingContact(BaseContact):
    contact = models.OneToOneField(Contact)

    class Meta(object):
        verbose_name = _('Billing Contact')
        verbose_name_plural = _('Billing Contacts')

    def __unicode__(self):
        return '%s (Bill: %s)' % (self.contact.name, self.name)


class AdministrativeContact(BaseContact):
    contact = models.OneToOneField(Contact)

    class Meta(object):
        verbose_name = _('Administrative Contact')
        verbose_name_plural = _('Administrative Contacts')

    def __unicode__(self):
        return '%s (Admin: %s)' % (self.contact.name, self.name)


class TechnicalContact(BaseContact):
    contact = models.OneToOneField(Contact)

    class Meta(object):
        verbose_name = _('Technical Contact')
        verbose_name_plural = _('Technical Contacts')

    def __unicode__(self):
        return '%s (Tech: %s)' % (self.contact.name, self.name)



