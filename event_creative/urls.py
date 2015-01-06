from django.conf.urls import patterns, url
from django.views.decorators.cache import cache_page
from views import *

n = 60*60*24

urlpatterns = patterns(
    'event_creative.urls',
    url(r'^$', cache_page(n)(Index.as_view()), name='main_page'),
    url(r'^articles/$', cache_page(n)(ArticleList.as_view()), name='article_list'),
    # url(r'^contacts/$', Contacts.as_view(), name='contacts'),
    url(r'^article/(?P<pk>[0-9]{1,3})/$', cache_page(n)(ArticleDetail.as_view()), name='article'),
    url(r'^services/$', cache_page(n)(ServicesList.as_view()), name='service_list'),
    url(r'^reports/$', cache_page(n)(ReportList.as_view()), name='report_list'),
    url(r'^report/(?P<pk>[0-9]{1,3})/$', cache_page(n)(ReportDetail.as_view()), name='report'),
)