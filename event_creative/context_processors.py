from models import Article, Report
from django.core.urlresolvers import resolve


def global_context(request):
    context = {'random_report': Report.objects.filter(active=True).order_by('?').first()}
    if resolve(request.path).url_name != 'article_list':
        context['articles_block'] = Article.objects.filter(active=True).order_by('-update_date')[:3]
    return context