#-*- coding:utf-8 -*-
from django.db import models

# Create your models here.
class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __unicode__(self):
        return self.full_name

class Article(models.Model):
    """
    文章
    """
    pub_date = models.DateTimeField('添加日期')
    headline = models.CharField('标题',max_length=200)
    article = models.TextField('文章')
    reporter = models.ForeignKey(Reporter)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'

    def __unicode__(self):
        return '%s' % (self.headline)
