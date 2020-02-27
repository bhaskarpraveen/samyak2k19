# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from cart import settings
# Create your models here.
class instamojo(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,)
    payment_id=models.CharField(max_length=50)
    amount=models.FloatField()
    purpose=models.CharField(max_length=50)
    status=models.CharField(max_length=15)
    payment_done=models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
