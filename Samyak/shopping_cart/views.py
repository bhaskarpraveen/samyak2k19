from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404

from users.models import Profile
from products.models import Product

from shopping_cart.extras import generate_order_id, transact, generate_client_token
from shopping_cart.models import OrderItem, Order, Transaction

import datetime
import stripe


from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.conf import settings

from paytm import Checksum


from paytm.models import PaytmHistory

def get_user_pending_order(request):
    # get order for the correct user
    user_profile = get_object_or_404(Profile, user=request.user)
    order = Order.objects.filter(owner=user_profile, is_ordered=False)
    if order.exists():
        # get the only order in the list of filtered orders
        return order[0]
    return 0


@login_required()
def add_to_cart(request, **kwargs):
    # get the user profile
    user_profile = get_object_or_404(Profile, user=request.user)
    # filter products by id
    product = Product.objects.filter(id=kwargs.get('item_id', "")).first()
    check=Profile.objects.filter(ebooks=product).count()
    if check>=product.limit:
        messages.info(request, 'Slots filled')
        return redirect(reverse('newapp:events')) 
    # check if the user already owns this product
    if product in request.user.profile.ebooks.all():
        messages.info(request, 'You already own this ebook')
        return redirect(reverse('newapp:events')) 
    # create orderItem of the selected product
    order_item, status = OrderItem.objects.get_or_create(product=product)
    # create order associated with the user
    user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
    user_order.items.add(order_item)
    if status:
        # generate a reference code
        user_order.ref_code = generate_order_id()
        user_order.save()

    # show confirmation message and redirect back to the same page
    messages.info(request, "item added to cart")
    if product.eventType == 'T':
        return redirect(reverse('products:product-list'))
    elif product.eventType == 'W':
        return redirect(reverse('products:workshops'))
    elif product.eventType == 'N':
        return redirect(reverse('products:nonTechnical'))
    elif product.eventType == 'D':
        return render(reverse('products:departmentevents'))


@login_required()
def delete_from_cart(request, item_id):
    item_to_delete = OrderItem.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        messages.info(request, "Item has been deleted")
    return redirect(reverse('shopping_cart:order_summary'))


@login_required()
def order_details(request, **kwargs):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order
    }
    return render(request, 'shopping_cart/order_summary.html', context)


@login_required()
def checkout(request, **kwargs):    
    pass

from django.template.loader import render_to_string


from django.core.mail import send_mail
from users.models import regPayment
@login_required
def update_registration(request,token):
    user=request.user
    if user.college=='1':

        r=regPayment(student=user.samyak_id,reg_paymentType='4',token_id=token,Amount=200)
    else:
        r=regPayment(student=user.samyak_id,reg_paymentType='4',token_id=token,Amount=500)
    r.save() 
    subject = 'Your Payment'
    message = 'You have succesfully registered for the events' + ' your Token number -'+str(token)
    user.email_user(subject, message)
    
    
    return redirect('newapp:events')
    

@login_required()
def update_transaction_records(request, token):
    # get the order being processed
    try:
        order_to_purchase = get_user_pending_order(request)

        # update the placed order
        order_to_purchase.is_ordered=True
        order_to_purchase.date_ordered=datetime.datetime.now()
        order_to_purchase.save()
        
        # get all items in the order - generates a queryset
        order_items = order_to_purchase.items.all()

        # update order items
        order_items.update(is_ordered=True, date_ordered=datetime.datetime.now())
        Order.objects.filter(items=order_items[0],owner=request.user.profile).update(ref_code=token)
        # Add products to user profile
        user_profile = get_object_or_404(Profile, user=request.user)
        # get the products from the items
        order_products = [item.product for item in order_items]
        user_profile.ebooks.add(*order_products)
        user_profile.save()
        for product in order_products:
            p=Profile.objects.filter(ebooks=product).count()
            if p>=product.limit:
                u=Product.objects.filter(name=product).update(limit_exceeded=True)
            else:
                u=Product.objects.filter(name=product).update(limit_exceeded=False)
            n=Product.objects.filter(name=product).update(numberofreg=p)
        # create a transaction
        transaction = Transaction.objects.create(profile=request.user.profile,
                                token=token,
                                order_id=order_to_purchase.id,
                                amount=order_to_purchase.get_cart_total(),
                                success=True)
        # save the transcation (otherwise doesn't exist)
        
        transaction.items.add(*order_products)
        user=request.user
        subject = 'Your Payment'
        message = render_to_string('payments_mail.html', {
            'user': user,
            'events':user_profile.ebooks.all(),
            'order':order_products,
            'transaction':transaction,
            
        })
        user.email_user(subject, message)
        # send an email to the customer
        # look at tutorial on how to send emails with sendgrid
        messages.info(request, "Thank you! Your purchase was successful!")
        return redirect(reverse('accounts:my_profile'))
    except:
        return redirect('accounts:my_profile')


def success(request, **kwargs):
    # a view signifying the transcation was successful
    return render(request, 'shopping_cart/purchase_success.html', {})
