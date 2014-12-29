from django.contrib import admin
from models import Article, Report


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'active', 'update_date')
    list_filter = ('update_date', )


class ReportAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'active', 'main_show', 'update_date')
    list_filter = ('update_date', 'main_show')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Report, ReportAdmin)