from django.contrib import admin
from models import Article, Report, Services, ImageTable


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

admin.site.register(Article, ArticleAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Services, ServiceAdmin)
admin.site.register(ImageTable)