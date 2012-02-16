from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'photostudio.views.home', name='home'),
    # url(r'^photostudio/', include('photostudio.foo.urls')),

    url(r'^$', 'photostudio.photo.views.home', name='home'),
    url(r'^uploadphotos/$', 'photostudio.photo.views.uploadphotos', name='upload'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/', include('registration.urls')),

    url(r'^uploadify/', include('uploadify.urls')),

)
