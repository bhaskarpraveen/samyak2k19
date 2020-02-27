from django.conf import settings
from django.db import models
from django.db.models.signals import post_save

from products.models import Product

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Max

CHOICES = [('1', 'KLU'),('2', 'OTHER')]
G_CHOICES=[('1','MALE'),('2','FEMALE'),('3','OTHER')]
REG_PAYMENT_TYPE=[('1','CASH'),('2','UPI'),('3','CARD'),('4','ONLINE'),('5','BANK')]
REG_PAYMENT_METHOD=[('2','ONLYREGPAYMENT'),('1','ONLYWORKSHOPS'),('3','REGANDWORKSHOPS'),('4','ACCOMODATION')]
def sk_id():
    p=CustomUser.objects.aggregate(Max('samyak_id'))['samyak_id__max']
    i=int(p[7::])+1
    u="SMK2K"
    c=1900000
    u=u+str(i+c)
    return u

class regPayment(models.Model):
    student=models.CharField(max_length=12,default=' ')
    reg_paymentType=models.CharField(max_length=1,choices=REG_PAYMENT_TYPE,null=False,default='3')
    Amount=models.IntegerField()
    token_id=models.CharField(max_length=50,blank=True)
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.student

from django.core.validators import RegexValidator
alphanumeric = RegexValidator(r'^[a-zA-Z ]*$', 'Only alphanumeric characters are allowed.')
from django.core.validators import MaxValueValidator
class CustomUser(AbstractUser):
    fullname=models.CharField(max_length=50, blank=True, null=True, validators=[alphanumeric])
    email = models.EmailField(unique=True)
    phonenumber= models.PositiveIntegerField(blank=True, validators=[MaxValueValidator(9999999999)],null=True)
    gender = models.CharField(max_length=1,choices=G_CHOICES,null=False,default='1')
    college = models.CharField(max_length=1,choices=CHOICES,null=False,default='2')
    id_number=models.CharField(default='18003000',max_length=20)
    college_name=models.CharField(max_length=30,null=True,blank=True)
    samyak_id=models.CharField(max_length=12,default=sk_id)
    reg_amount=models.BooleanField(default=False)
    amb_candid=models.ManyToManyField(settings.AUTH_USER_MODEL)
    is_amb=models.BooleanField(default=False)
    can_amb=models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    # add additional fields in here

    def __str__(self):
        return self.username
    

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ebooks = models.ManyToManyField(Product, blank=True)
    stripe_id = models.CharField(max_length=200, null=True, blank=True)
    email_confirmed = models.BooleanField(default=False)
    reg_payment=models.BooleanField(default=False)
    reg_paymethod= models.CharField(max_length=1,choices=REG_PAYMENT_METHOD,null=False,default='3')

    def __str__(self):
        return self.user.username


def post_save_profile_create(sender, instance, created, *args, **kwargs):
    user_profile, created = Profile.objects.get_or_create(user=instance)

    if user_profile.stripe_id is None or user_profile.stripe_id == '':
        new_stripe_id = stripe.Customer.create(email=instance.email)
        user_profile.stripe_id = new_stripe_id['id']
        user_profile.save()


post_save.connect(post_save_profile_create, sender=settings.AUTH_USER_MODEL)
