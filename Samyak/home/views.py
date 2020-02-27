from django.shortcuts import render
from products.models import Product
# Create your views here.


# Create your views here.

  
from django.shortcuts import render, redirect
from django.views import generic

from .forms import (
    BookFormset,
    BookModelFormset,
    BookModelForm,
    AuthorFormset
)
from .models import Book, Author

def create_book_normal(request):
    template_name = 'store/create_normal.html'
    heading_message = 'Formset Demo'
    if request.method == 'GET':
        formset = BookFormset(request.GET or None)
    elif request.method == 'POST':
        formset = BookFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                name = form.cleaned_data.get('name')
                # save book instance
                if name:
                    Book(name=name).save()
            return redirect('home:book_list')

    return render(request, template_name, {
        'formset': formset,
        'heading': heading_message,
    })


class BookListView(generic.ListView):

    model = Book
    context_object_name = 'books'
    template_name = 'store/list.html'


def create_book_model_form(request):
    template_name = 'store/create_normal.html'
    heading_message = 'Model Formset Demo'
    if request.method == 'GET':
        formset = BookModelFormset(queryset=Book.objects.none())
    elif request.method == 'POST':
        formset = BookModelFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                # only save if name is present
                if form.cleaned_data.get('name'):
                    form.save()
            return redirect('home:book_list')

    return render(request, template_name, {
        'formset': formset,
        'heading': heading_message,
    })
from django.http import HttpResponse
from django.contrib import messages
from users.models import CustomUser
def create_book_with_authors(request):
    template_name = 'store/create_with_author.html'
    asuccess=False
    csuccess=False
    errors=[]
    if request.method == 'GET':
        bookform = BookModelForm(request.GET or None)
        formset = AuthorFormset(queryset=Author.objects.none())
    elif request.method == 'POST':
        bookform = BookModelForm(request.POST)
        formset = AuthorFormset(request.POST)
        
        if bookform.is_valid() and formset.is_valid():
            user_sk_id=bookform.cleaned_data['name']
            
            amb_id=CustomUser.objects.filter(samyak_id=user_sk_id,can_amb=True)
            
            if amb_id :
                asuccess=True
                book = bookform.save()
            # first save this book, as its reference will be used in `Author`
                c_list=[]
                for form in formset:
                    
                    try:
                        
                        candidate_id=form.cleaned_data['name']
                        candidate_mail=form.cleaned_data['mail']
                        con_id=CustomUser.objects.get(samyak_id=candidate_id,email=candidate_mail,can_amb=True)
                        c_list.append(candidate_id)
                    except :
                        con_id=0
                        errors.append(candidate_id+'error')
                    
                    

                    if not con_id and len(c_list)< 3:
                        return HttpResponse(candidate_id+'failed')
                if len(c_list)>=3:
                    for i in c_list:
                        CustomUser.objects.filter(samyak_id=i).update(can_amb=False)
                        f=CustomUser.objects.get(samyak_id=i)
                        con_id.amb_candid.add(f)
                    CustomUser.objects.filter(samyak_id=user_sk_id).update(is_amb=True)
                    CustomUser.objects.filter(samyak_id=user_sk_id).update(can_amb=False)
                    csuccess=True
                    
                    return HttpResponse('We will get back to you soon :)')


        
                
    return render(request, template_name, {
        'bookform': bookform,
        'formset': formset,
        'errors':errors,

        
    })
