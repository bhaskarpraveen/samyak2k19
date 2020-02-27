from django import forms 
from .models import *
from .models import Product

class ProductForm(forms.ModelForm):

    class Meta:
        model=Product
        fields='__all__'