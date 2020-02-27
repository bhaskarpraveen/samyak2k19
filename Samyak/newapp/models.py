from django.db import models
import datetime
# Create your models here.

class Notification(models.Model):
    notification=models.CharField(max_length=200)
    date=models.CharField(max_length=2,default='27')
    month=models.CharField(max_length=4,default='SEPT')
    def __str__(self):
        return self.notification
class Dashpost(models.Model):
    title=models.CharField(max_length=30,default='samyak')
    img=models.ImageField(upload_to='images/')
    description=models.CharField(max_length=1000)
    date = models.DateTimeField(default=datetime.datetime.now)
    def __str__(self):
        return self.title
TIME_CHOICES=[('1','24'),('2','48')]
from users.models import CustomUser
from cart import settings
