from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from search.views import search
from search.views import response
from search.views import socialmedia


admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', '_400.views.home', name='home'),
    # url(r'^_400/', include('_400.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'social_media$',socialmedia),
    url(r'^search$', search),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root' : settings.STATIC_ROOT,}),
    url(r'^search/jobtitle$',response),

)
