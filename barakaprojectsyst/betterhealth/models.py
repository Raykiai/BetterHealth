from datetime import date
from django.db import models

from django import db
db.connections.close_all()

# Create your models here.
class RecordInfo(models.Model):
    
    pid = models.IntegerField(default= 0)
    date = models.CharField(max_length=200)
    fname = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    sex = models.CharField(max_length=200, default="")
    weight = models.CharField(max_length=200)
    wCategory = models.CharField(max_length=200)
    height = models.CharField(max_length=200)
    hCategory = models.CharField(max_length=200)
    def __str__(self):
        return self.pid

class ChildInfo(models.Model):
    dob = models.CharField(max_length=200)
    fname = models.CharField(max_length=200)
    sex = models.CharField(max_length=200)
    cname = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    residence = models.CharField(max_length=200)
    def __str__(self):
        return self.fname

class DiagnosisInfo(models.Model):
    pid = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    fname = models.CharField(max_length=200)
    nid = models.CharField(max_length=200)
    diagnosis = models.CharField(max_length=200)
    def __str__(self):
        return self.pid


class Author(models.Model):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    def __unicode__(self):
        return self.question