from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.conf import settings

from . import Checksum
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404

from .models import PaytmHistory
from shopping_cart.views import get_user_pending_order
from users.models import Profile,CustomUser
# Create your views here.




@login_required
def registrationPayment(request,**kwargs):
    if not request.user.reg_amount:
        user = request.user
        settings.USER = user
        MERCHANT_KEY = settings.PAYTM_MERCHANT_KEY
        MERCHANT_ID = settings.PAYTM_MERCHANT_ID
        CALLBACK_URL = settings.HOST_URL + settings.PAYTM_CALLBACK_URL
        # Generating unique temporary ids
        order_id = Checksum.__id_generator__()
        up=Profile.objects.filter(user=settings.USER).update(reg_paymethod='2')
        if user.college=='1':
            bill_amount = 200
        else:
            bill_amount=500
        if bill_amount:
            data_dict = {
                'MID': MERCHANT_ID,
                'ORDER_ID': order_id,
                'TXN_AMOUNT': bill_amount,
                'CUST_ID': user.email,
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': settings.PAYTM_WEBSITE,
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL': CALLBACK_URL,
            }
            param_dict = data_dict
            param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(data_dict, MERCHANT_KEY)
            return render(request, "payment.html", {'paytmdict': param_dict, 'user': user})
        return HttpResponse("Bill Amount Could not find. ?bill_amount=10")
    else:
        return redirect(reverse('newapp:events'))

@login_required
def payment(request, **kwargs):
    user = request.user
    settings.USER = user
    MERCHANT_KEY = settings.PAYTM_MERCHANT_KEY
    MERCHANT_ID = settings.PAYTM_MERCHANT_ID
    CALLBACK_URL = settings.HOST_URL + settings.PAYTM_CALLBACK_URL
    # Generating unique temporary ids
    order_id = Checksum.__id_generator__()
    existing_order = get_user_pending_order(request)
    bill_amount = existing_order.get_cart_total()
    up=Profile.objects.filter(user=settings.USER).update(reg_paymethod='1')
    if user.college=='2' and not user.reg_amount:
        bill_amount=bill_amount+500
        user.profile.reg_payment=True
        Profile.objects.filter(user=user).update(reg_paymethod='3')
    
    if bill_amount:
        data_dict = {
            'MID': MERCHANT_ID,
            'ORDER_ID': order_id,
            'TXN_AMOUNT': bill_amount,
            'CUST_ID': user.email,
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': settings.PAYTM_WEBSITE,
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL': CALLBACK_URL,
        }
        param_dict = data_dict
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(data_dict, MERCHANT_KEY)
        return render(request, "payment.html", {'paytmdict': param_dict, 'user': user})
    return HttpResponse("Bill Amount Could not find. ?bill_amount=10")



@csrf_exempt
def response(request):
    if request.method == "POST":
        MERCHANT_KEY = settings.PAYTM_MERCHANT_KEY
        data_dict = {}
        for key in request.POST:
            data_dict[key] = request.POST[key]
        verify = Checksum.verify_checksum(data_dict, MERCHANT_KEY, data_dict['CHECKSUMHASH'])
        if verify:
            for key in request.POST:
                if key == "BANKTXNID" or key == "RESPCODE":
                    if request.POST[key]:
                        data_dict[key] = int(request.POST[key])
                    else:
                        data_dict[key] = 0
                elif key == "TXNAMOUNT":
                    data_dict[key] = float(request.POST[key])
            if data_dict['STATUS']=='TXN_FAILURE':
                return redirect('newapp:events')
            PaytmHistory.objects.create(user=settings.USER, **data_dict)
            tid=PaytmHistory.objects.get(user=settings.USER, **data_dict)
            i=tid.ORDERID
            user=settings.USER
            if user.profile.reg_paymethod=='1' : 
                return redirect(reverse('shopping_cart:update_records',
                            kwargs={
                                'token': i
                            })
                        )
            elif user.profile.reg_paymethod=='2':
                up=CustomUser.objects.filter(username=settings.USER).update(reg_amount=True)
                return redirect(reverse('shopping_cart:update_registration',
                        kwargs={
                            'token': i
                        })
                  )
            elif user.profile.reg_paymethod=='3':
                up=CustomUser.objects.filter(username=settings.USER).update(reg_amount=True)
                subject = 'Your Payment'
                message='Hi ' + str(user.username)+' '+'your samyak id : '+str(user.samyak_id)+'  ,'+'you have been successfully registered to all events(*This doesn\'t include workshops)'
                send_mail(subject,message,'techsamyak19@gmail.com',[user.email],fail_silently=False)
                return redirect(reverse('shopping_cart:update_records',
                                kwargs={
                                    'token': i,

                                })
                            )
            
           
        else:
            return HttpResponse("checksum verify failed")
    return HttpResponse(status=200)
