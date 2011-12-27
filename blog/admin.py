
__author__ = 'Lishiguang'

from django.contrib import admin
from webblog.blog.models import Reporter,Article

admin.site.register(Reporter)
admin.site.register(Article)