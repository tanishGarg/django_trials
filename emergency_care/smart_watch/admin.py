# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

# Register your models here.
from .models import Person_information, Care_giver, Watch_Information

class Watch_Information_Admin(admin.ModelAdmin):
    fieldsets = [
        ('Owner',                  {'fields' : ['person']}),
        ('P_information',          {'fields' : ['heart_beat', 'step', 'distance', 'hospital', 'pub_date'], 'classes':['collapse']}),
    ]
    list_display = ('person','pub_date')
    list_filter = ['pub_date']
    search_fields = ['person__name']


admin.site.register(Person_information)
admin.site.register(Care_giver)
admin.site.register(Watch_Information,Watch_Information_Admin)
