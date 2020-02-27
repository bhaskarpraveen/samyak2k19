from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from . import views
app_name='administration'
urlpatterns = [
    path('',admin_main,name='admin_main'),
    path('update/',update,name='update'),
    path('signup/',signup,name='signup'),
    path('allusers/',allUsers,name='allUsers'),
    path('registration-payments/',regPayments,name='regPayments'),
    path('export/',export,name='export'),
    path('logout/',logout_view,name='logout'),
    path('change/',change,name='change'), 
    path('superactivate/',superactivate,name='superactivate'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
