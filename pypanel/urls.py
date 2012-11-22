from django.conf.urls import patterns, include, url
from session_csrf import anonymous_csrf

from django.contrib import admin
admin.autodiscover()


def bad(request):
    """ Simulates a server error. """
    1 / 0


urlpatterns = patterns('',
    url(r'^$', include('pypanel.base.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^bad/$', bad),
)
