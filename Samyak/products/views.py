from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from shopping_cart.models import Order
from .models import Product
import sys
import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

def product_list(request):
    amount=500
    if request.user.is_authenticated:
        if request.user.college=='1':
            amount=200
    else:
            amount=500
    
    object_list = Product.objects.filter(eventType='T')
    try:
        filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered=False)
        current_order_products = []
        if filtered_orders.exists():
            user_order = filtered_orders[0]
            user_order_items = user_order.items.all()
            current_order_products = [product.product for product in user_order_items]
        context = {
        'object_list': object_list,
        'current_order_products': current_order_products,
        'amount':amount
        }
    except:

        context = {
            'object_list': object_list,
            #'current_order_products': current_order_products
            'amount':amount
        }
    return render(request, "techevents.html", context)


def nonTechnical(request):
    amount=500
    if request.user.is_authenticated:
        if request.user.college=='1':
            amount=200
    else:
        amount=500
    object_list = Product.objects.filter(eventType='N')
    try:
        filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered=False)
        current_order_products = []
        if filtered_orders.exists():
            user_order = filtered_orders[0]
            user_order_items = user_order.items.all()
            current_order_products = [product.product for product in user_order_items]

        context = {
            'object_list': object_list,
            'current_order_products': current_order_products,
            'amount':amount
        }
    except:
        context={
            'object_list': object_list,
            'amount':amount
        }

    return render(request, "nontechevents.html", context)
def workshops(request):
    amount=500
    if request.user.is_authenticated:
        if request.user.college=='1':
            amount=200
    else:
        amount=500
    object_list = Product.objects.filter(eventType='W')
    if request.GET.get('featured'):
        featured_filter = request.GET.get('featured')
        if featured_filter=='A':
            object_list = Product.objects.filter(eventType='W')
        else:
            object_list = Product.objects.filter(branchType=featured_filter,eventType='W')
    try:
        filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered=False)
        current_order_products = []
        if filtered_orders.exists():
            user_order = filtered_orders[0]
            user_order_items = user_order.items.all()
            current_order_products = [product.product for product in user_order_items]

        context = {
            'object_list': object_list,
            'current_order_products': current_order_products,
            'amount':amount

        }
    except:
        context={
            'object_list': object_list,
            'amount':amount

        }

    return render(request, "workshops.html", context)
def paperpresen(request):
    return render(request,'paperpresentation.html',{})
def departmentevents(request):
    amount=500
    if request.user.is_authenticated:
        if request.user.college=='1':
            amount=200
    else:
        amount=500
    object_list = Product.objects.filter(eventType='D')
    featured_filter=0
    if request.GET.get('featured'):
        featured_filter = request.GET.get('featured')
        if featured_filter=='A':
            object_list = Product.objects.filter(eventType='D')
        else:
            object_list = Product.objects.filter(branchType=featured_filter,eventType='D')
    try:
        filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered=False)
        current_order_products = []
        if filtered_orders.exists():
            user_order = filtered_orders[0]
            user_order_items = user_order.items.all()
            current_order_products = [product.product for product in user_order_items]

        context = {
            'object_list': object_list,
            'current_order_products': current_order_products,
            'featured_filter':featured_filter,
            'amount':amount

        }
    except:
        context={
            'object_list': object_list,
            'featured_filter':featured_filter,
            'amount':amount

        }
    return render(request,'departmentevents.html',context)
def literaryEvents(request):
    amount=500
    if request.user.is_authenticated:
        if request.user.college=='1':
            amount=200
    else:
        amount=500
    object_list = Product.objects.filter(eventType='L')
    try:
        filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered=False)
        current_order_products = []
        if filtered_orders.exists():
            user_order = filtered_orders[0]
            user_order_items = user_order.items.all()
            current_order_products = [product.product for product in user_order_items]

        context = {
            'object_list': object_list,
            'current_order_products': current_order_products,
            'amount':amount
        }
    except:
        context={
            'object_list': object_list,
            'amount':amount
        }

    return render(request, "literaryevents.html", context)
