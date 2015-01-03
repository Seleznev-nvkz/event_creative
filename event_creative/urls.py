from django.conf.urls import patterns, url
from views import *

urlpatterns = patterns(
    'event_creative.urls',
    url(r'^$', Index.as_view(), name='main_page'),
    url(r'^articles/$', ArticleList.as_view(), name='article_list'),
    # url(r'^contacts/$', Contacts.as_view(), name='contacts'),
    url(r'^article/(?P<pk>[0-9]{1,3})/$', ArticleDetail.as_view(), name='article'),
    url(r'^services/$', ServicesList.as_view(), name='service_list'),
    url(r'^reports/$', ReportList.as_view(), name='report_list'),
    url(r'^report/(?P<pk>[0-9]{1,3})/$', ReportDetail.as_view(), name='report'),
)