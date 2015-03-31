from django.contrib import admin
from models import Article, Report, Services, ImageTable, Price
from django.contrib.admin.views.decorators import staff_member_required
from django.http.response import HttpResponseRedirect
from django.conf.urls import patterns, url
from django.db.models import Q


@staff_member_required
def export(request):
    ImageTable.objects.filter(Q(price_slider__isnull=True) &
                              Q(services_slider__isnull=True) &
                              Q(report_slider__isnull=True)).delete()
    return HttpResponseRedirect(request.META["HTTP_REFERER"])


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'active', 'update_date')
    list_filter = ('update_date', )


class ReportAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'active', 'main_show', 'update_date')
    filter_horizontal = ('slider', )
    list_filter = ('update_date', 'main_show')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'active', 'update_date')
    filter_horizontal = ('slider', )
    list_filter = ('update_date', )


class PriceAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'active', )
    filter_horizontal = ('slider', )
    list_filter = ('active', )


class ImageTableAdmin(admin.ModelAdmin):

    def get_urls(self):
        urls = super(ImageTableAdmin, self).get_urls()
        my_urls = patterns("", url(r"^clear_image/$", export))
        return my_urls + urls

admin.site.register(Article, ArticleAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Services, ServiceAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(ImageTable, ImageTableAdmin)