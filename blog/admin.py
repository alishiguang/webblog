
__author__ = 'Lishiguang'

from django.contrib import admin
from webblog.blog.models import Reporter,Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('headline','article','pub_date')
    list_filter = ('pub_date',)
    ordering = ('-pub_date',)
    class Media:
        js=('/site_media/js/tiny_mce/tiny_mce.js','/site_media/js/textareas.js')

admin.site.register(Reporter)
admin.site.register(Article,ArticleAdmin)