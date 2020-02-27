from django.urls import re_path
from .views import  payment, response,registrationPayment
app_name='Paytm'
urlpatterns = [

    
    re_path(r'^payment/', payment, name='payment'),
    re_path(r'^response/', response, name='response'),
    re_path(r'^registrationpayment/',registrationPayment, name='registrationpayment'),

]
