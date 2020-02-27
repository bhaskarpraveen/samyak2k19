from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import *
from django.template import  loader
from django.http import HttpResponse
from .models import Dashpost,Notification
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView
# Create your views here.
import sys
import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
from firebase_admin import db
from firebase_admin import auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
def main(request):
    return render(request,'home.html',{})
def pretechnical(request):
        amount=500
        if request.user.is_authenticated:
                if request.user.college=='1':
                        amount=200
        else:
                amount=500
        
        return render(request,'pretechnical.html',{'amount':amount})
def events(request):
        if request.user.is_authenticated:
                if request.user.college=='1':
                        amount=200
                else:
                        amount=500
        else:
                amount=500
        return render(request,'preevents.html',{'amount':amount})
def contact(request):
    return render(request,'contact.html',{})
def dash(request):
        post=Dashpost.objects.order_by('-date')
        notif=Notification.objects.all()
        page = request.GET.get('page', 1)

        paginator = Paginator(post, 10)
        try:
                posts = paginator.page(page)
        except PageNotAnInteger:
                posts = paginator.page(1)
        except EmptyPage:
                posts = paginator.page(paginator.num_pages)

        return render(request,'dashboard.html',{
                'post':posts,
                'not':notif,
                        })


def about(request):
    return render(request,'about.html',{})
def tech(request):
    return render(request,'techevents.html',{})
def proshow(request):
    return render(request,'proshow.html',{})
def sponsors(request):
    return render(request,'sponsors.html',{})
def gallery(request):
    return render(request,'gallery.html',{})
def team(request):
        return render(request,'team.html',{})
def explore_17(request):
        return render(request,'explore17.html',{})
def explore_18(request):
        return render(request,'explore18.html',{})
def explore_19(request):
        return render(request,'explore19.html',{})
from django.views.generic.edit import FormView
from products.forms import ProductForm
from django.template import  loader
from products.models import Product
def allevents(request):

        if request.method == 'POST':
                form = ProductForm(request.POST, request.FILES)

                if form.is_valid():
                        form.save()
                        name=form.cleaned_data['name']
                        img=form.cleaned_data['displayImage']
                        bucket=firebase_admin.storage.bucket()
                        image=requests.get('http://127.0.0.1:8000/media/images/4k-wallpaper-astro-astrology-1146134_hc3tK1I.jpg').content
                        blob=bucket.blob(name+'.jpg')
                        blob.upload_from_string(image,content_type='images/jpg')
                        ref=db.reference('Events/tech')
                        ref.push({
                                'name':name,
                                'img':blob.public_url
                        })

                        return redirect('newapp:success')
        else:
                form = ProductForm()
        return render(request, 'allevents.html', {'form':form})


def success(request):
	return HttpResponse('successfuly uploaded')
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

class ArticleListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'article_list.html'

class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'article_detail.html'



class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = '__all__'
    template_name = 'article_edit.html'
    def test_func(self):
        return True


    # def dispatch(self, request, *args, **kwargs):
    #     obj = self.get_object()
    #     if obj.author != self.request.user:
    #         raise PermissionDenied
    #     return super().dispatch(request, *args, **kwargs)


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'article_delete.html'
    success_url = reverse_lazy('newapp:article_list')
    def test_func(self):
        return True


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'article_new.html'
    fields = '__all__'
    login_url = 'login'

def posterpresentation(request):
    return render(request,'posterpresentation.html',{})

def prototypeexpo(request):
    return render(request,'prototypeexpo.html',{})

def accomodation(request):
    return render(request,'accomodation.html',{})

def mycertificates(request):
    return render(request,'mycertificates.html',{})
