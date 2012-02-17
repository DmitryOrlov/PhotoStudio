from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'photo.views.uploadphotos', name='uploadphotos'),
    url(r'^receiver/$', 'photo.views.filesreceiver', name='receiver'),
)
