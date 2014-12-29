from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns(
    '',
    url(r'^redactor/', include('redactor.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('event_creative.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)

urlpatterns += staticfiles_urlpatterns()