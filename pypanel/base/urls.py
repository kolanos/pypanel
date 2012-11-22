from django.conf.urls.defaults import url, patterns


urlpatterns = patterns('pypanel.base.views',
    url(r'^$', 'home', name='home'),
)
