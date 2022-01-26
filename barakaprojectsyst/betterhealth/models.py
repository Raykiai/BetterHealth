from django.db import models

# Create your models here.
class RecordInfo(models.Model):
    date = models.CharField(max_length=200)
    fname = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    weight = models.CharField(max_length=200)
    wCategory = models.IntegerField()
    height = models.CharField(max_length=200)
    hCategory = models.IntegerField()
    bFeeding =models.CharField(max_length=200)
    suppliment = models.CharField(max_length=200)
    development = models.CharField(max_length=200)

    def __str__(self):
        return self.date

class Author(models.Model):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    def __unicode__(self):
        return self.question