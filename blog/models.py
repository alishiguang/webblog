from django.db import models

# Create your models here.
class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name
    class Admin:
        pass

class Article(models.Model):
    pub_date = models.DateTimeField()
    headline = models.CharField(max_length=200)
    article = models.TextField()
    reporter = models.ForeignKey(Reporter)

    def __str__(self):
        return self.headline
    class Admin:
        pass