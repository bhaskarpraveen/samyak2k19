# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models

from django.db.models import Count

from django.contrib.auth.models import User
from django.urls import reverse
Type_CHOICE=[('T','Technical'),('N','NonTechnical'),('W','Workshop'),('D','DepartmentEvents'),('L','LiteraryEvents')]
BRANCH_CHOICE=[('C','CSE'),('E','ECE'),('EEE','EEE'),('ECM','ECM'),('MEC','MECHANICAL'),('CIV','CIVIL'),('FA','FINEARTS'),('BT','BIOTECH'),('PH','PHARMACY'),('DCA' ,'DEPARTMENT  OF COMPUTER APPLICATIONS'),('HM','HOTEL MANAGEMENT'),('BS','BUSINESS SCHOOL'),('SA','SCHOOL OF ARCHITECTURE'),('CC','COLLEGE OF COMMERCE'),('SL','SCHOOLOFLAW'),('FED','FED'),('DC','DEPARTMENTOFCHEMISTRY'),('DA','DEPARTMENTOFARTS(B-A-IAS)'),('O','OTHERS')]



class Co_ordinator(models.Model):
    Cname=models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.Cname
class Faculty(models.Model):
    Fname=models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.Fname


class Product(models.Model):
    name = models.CharField(max_length=120)
    displayImage=models.ImageField(upload_to='images/')
    price = models.IntegerField()
    datentime=models.CharField(max_length=50,null=True)
    description=models.TextField(max_length=500,null=True)
    eventType=models.CharField(max_length=1,choices=Type_CHOICE,null=True)
    branchType=models.CharField(max_length=3,choices=BRANCH_CHOICE,null=True)
    co_ordinator = models.ForeignKey(Co_ordinator,null=True,on_delete=models.CASCADE)
    co_ordinator_ph=models.IntegerField(null=True)
    limit=models.IntegerField(default=1000)
    venue=models.CharField(max_length=50,null=True)
    faculty=models.ForeignKey(Faculty, on_delete=models.CASCADE,null=True)
    numberofreg=models.IntegerField(default=0)
    certificate_ditributed=models.BooleanField(default=False)
    eCertificate_distributed=models.BooleanField(default=False)
    limit_exceeded=models.BooleanField(default=False)
    display=models.IntegerField(null=True)
    def get_absolute_url(self):
        return reverse('newapp:article_detail', args=[str(self.id)])
   
    def __str__(self):
        return self.name
class Attendence(models.Model):
    event_name=models.OneToOneField(Product, on_delete=models.CASCADE)
    attendees=models.ManyToManyField(settings.AUTH_USER_MODEL)
    def __str__(self):
        return self.event_name.name
