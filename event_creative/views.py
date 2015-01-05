# -*- coding: utf-8 -*-
from models import Article, Report, Services
from django.views.generic import DetailView, ListView, TemplateView


class Index(TemplateView):
    """
    Главная страница
    """
    template_name = 'index_page.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['reports'] = Report.objects.filter(active=True, main_show=True).order_by('-update_date')[:3]
        return context


class ArticleList(ListView):
    """
    Список статей
    """
    template_name = 'article_list.html'
    queryset = Article.objects.filter(active=True).order_by('-update_date')
    context_object_name = 'articles'
    paginate_by = 10


class ArticleDetail(DetailView):
    """
    Статья подробно
    """
    template_name = 'article.html'
    model = Article
    context_object_name = 'article'


class ReportList(ListView):
    """
    Список отчетов
    """
    template_name = 'report_list.html'
    queryset = Report.objects.filter(active=True).order_by('-update_date')
    context_object_name = 'reports'
    paginate_by = 10


class ReportDetail(DetailView):
    """
    Отчет подробно
    """
    template_name = 'report.html'
    model = Report
    context_object_name = 'report'


class ServicesList(ListView):
    """
    Страница со списком услуг
    """
    template_name = 'services_list.html'
    queryset = Services.objects.filter(active=True).order_by('-update_date')
    context_object_name = 'services'
    paginate_by = 10


# class Contacts(TemplateView):
#     """
#     Страница со списком контактов
#     """
#     template_name = 'contacts.html'