from django.conf.urls import url

from . import views
app_name='apitest'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^pay/', views.create_payment_req, name="payment"),
    url(r'^list/', views.list_payments, name="list"),
    url(r'^registrationpayment/',views.registration_payments, name='registrationpayment'),
]
