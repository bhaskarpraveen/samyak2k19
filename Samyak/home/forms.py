from django import forms
from django.forms import (formset_factory, modelformset_factory)

from .models import (Book, Author)


class BookForm(forms.Form):
    name = forms.CharField(
        label='Ambassador Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Ambassador Name here'
        })
    )


class BookModelForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('name', )
        labels = {
            'name': 'Ambassador Name'
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Ambassador ID here'
                }
            )
        }


BookFormset = formset_factory(BookForm)
BookModelFormset = modelformset_factory(
    Book,
    fields=('name', ),
    extra=1,
    widgets={
        'name': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Ambassador ID here'
            }
        )
    }
)

AuthorFormset = modelformset_factory(
    Author,
    fields=('name','mail', ),
    extra=1,
    widgets={'name': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '           Member ID '
        }),
        'mail': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '           Member email'
        })
    }
)