from django import forms 
from products.models import Product
from .models import evePayment
from django.forms import ModelForm


class offPayments(ModelForm):
    user_id=forms.CharField(max_length=12)
    
    class Meta():
        model=evePayment
        fields=['name','user_id']

class activate(forms.Form):
    i=forms.CharField(max_length=12)


class AttendenceForm(forms.Form):
    samyak_id=forms.CharField(max_length=12)
