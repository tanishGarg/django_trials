#Models - to define layout of database and additional metadata


# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length = 200)#, default = 'wassup?
    pub_date= models.DateTimeField('date published')#, default = 0)
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now()-datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)#, default= 0
    choice_text= models.CharField(max_length=200) #, default = timezone.now()
    votes= models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
