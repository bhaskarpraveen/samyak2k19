from django.db import models
from products.models import Product
# Create your models here.
REG_PAYMENT_TYPE=[('3','CASH'),('2','UPI'),('1','CARD')]
class evePayment(models.Model):
    name=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    user_id=models.CharField(max_length=12,default=' ')
    price=models.IntegerField(null=True,blank=True)
    reg_paymentType=models.CharField(max_length=1,choices=REG_PAYMENT_TYPE,null=True,default='1')
    idnumber=models.CharField(max_length=12,default='')
    def __str__(self):
        return self.user_id
    
    
