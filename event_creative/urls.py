from django.conf.urls import patterns, url
from django.views.decorators.cache import cache_page
from views import *

urlpatterns = patterns(
    'event_creative.urls',
    url(r'^$', Index.as_view(), name='main_page'),
    url(r'^articles/$', cache_page(0)(ArticleList.as_view()), name='article_list'),
    # url(r'^contacts/$', Contacts.as_view(), name='contacts'),
    url(r'^article/(?P<pk>[0-9]{1,3})/$', cache_page(0)(ArticleDetail.as_view()), name='article'),
    url(r'^services/$', cache_page(0)(ServicesList.as_view()), name='service_list'),
    url(r'^reports/$', cache_page(0)(ReportList.as_view()), name='report_list'),
    url(r'^report/(?P<pk>[0-9]{1,3})/$', cache_page(0)(ReportDetail.as_view()), name='report'),
    url(r'^price/$', cache_page(0)(PriceView.as_view()), name='price'),
)