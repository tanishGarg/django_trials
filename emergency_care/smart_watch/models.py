# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Person_information(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Care_giver(models.Model):
    person = models.ForeignKey(Person_information, on_delete=models.CASCADE)
    care_giver_name= models.CharField(max_length=50) #, default = timezone.now()
    def __str__(self):
        return self.care_giver_name


class Watch_Information(models.Model):
    person = models.ForeignKey(Person_information, on_delete=models.CASCADE, default=0)
    heart_beat= models.IntegerField(default=0)
    step= models.IntegerField(default=0)
    distance= models.IntegerField(default=0)
    hospital= models.IntegerField(default=0)
    pub_date= models.DateTimeField('published')
