from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

'''
from django import template
register = template.Library()
@register.filter
def transto(value):
    return _(value)
'''

urlpatterns = patterns('',
    # Example:
    # (r'^webblog/', include('webblog.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^index/','blog.views.index'),
    (r'^register/','blog.views.register'),
    (r'^site_media/(?P<path>.*)$','django.views.static.serve',{'document_root': 'media'}),
)
