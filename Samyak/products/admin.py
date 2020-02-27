# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Product,Co_ordinator,Faculty,Attendence
from users.models import CustomUser 
from django.utils import timezone


admin.site.register(Product)
admin.site.register(Co_ordinator)
admin.site.register(Faculty)


class AttendenceAdmin(admin.ModelAdmin):
    model =Attendence
    list_display = ['event_name','TotalAttendees',]
    search_fields=('event_name__name',)
    filter_horizontal = ('attendees',)
    def TotalAttendees(self,obj):
        return obj.attendees.all().count()
    
admin.site.register(Attendence,AttendenceAdmin)