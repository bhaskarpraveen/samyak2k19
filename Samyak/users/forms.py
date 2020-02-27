from __future__ import unicode_literals
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import get_user_model
from django.core.validators import validate_email
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.core.exceptions import ValidationError

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
#from django.contrib.auth import get_user_model
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser,regPayment

class Payment(ModelForm):
    
    class Meta:
        model=regPayment
        fields=['student','reg_paymentType','Amount']

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        User=get_user_model()
        model = CustomUser
        fields = ('username','fullname', 'email','phonenumber','gender','college','college_name','id_number')
        widgets = {
            'username': forms.TextInput(attrs={

                'placeholder': 'Username'
                }
            ),
            'college_name': forms.TextInput(attrs={

                'placeholder': 'college name(If you\'re from other clg)'
                }
            ),
            'fullname': forms.TextInput(attrs={

                'placeholder': 'Full Name(This will be displayed in your certificate)'
                }
            ),
            'email': forms.TextInput(attrs={

                'placeholder': 'Email'
                }
            ),
            'phonenumber': forms.TextInput(attrs={

                'placeholder': 'Phone Number'
                }
            ),
            'id_number': forms.TextInput(attrs={

                'placeholder': 'id Number'
                }
            ),


        }

class CustomUserChangeForm(UserChangeForm):
    
    class Meta(UserChangeForm):
        User=get_user_model()
        model = CustomUser
        fields = ('username','fullname','email','gender','college','id_number')
#class SignUpForm(UserCreationForm):
 #   CHOICES = [('1', 'KLU'),('2', 'OTHER')]
  #  first_name = forms.CharField(max_length=30)
   # last_name = forms.CharField(max_length=30)
#    #email = forms.EmailField(max_length=254)
 #   college = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
  #  def clean_email(self):
   #     email = self.cleaned_data['email']
    #    if User.objects.filter(email=email).exists():
     #       raise ValidationError("Email already exists")
      #  return email
#    class Meta:
 #       model = User
  #      fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2','college' )
