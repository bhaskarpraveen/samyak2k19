# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import instamojo
# Register your models here.
class InstamojoAdmin(admin.ModelAdmin):
    model = instamojo
    list_display = ['user','payment_id','amount']
    search_fields=('user__username','payment_id','amount')
admin.site.register(instamojo,InstamojoAdmin)


