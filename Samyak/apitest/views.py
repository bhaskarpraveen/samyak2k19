from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .forms import PayForm
from instamojo_wrapper import Instamojo
from cart.settings import API_KEY,AUTH_TOKEN
from shopping_cart.views import get_user_pending_order
from django.contrib.auth.decorators import login_required
from .models import instamojo
from cart import settings
from django.shortcuts import redirect
api = Instamojo(api_key=API_KEY, auth_token=AUTH_TOKEN)
from users.models import Profile
@login_required()
def index(request):
    # if this is a POST request we need to process the form data
    
    user=request.user
    existing_order = get_user_pending_order(request)
    bill_amount = existing_order.get_cart_total()
    up=Profile.objects.filter(user=user).update(reg_paymethod='1')
    if user.college=='2' and not user.reg_amount:
        bill_amount=bill_amount+500
        Profile.objects.filter(user=user).update(reg_paymethod='3')
    response = api.payment_request_create(
        amount=str(bill_amount),
        purpose='Samyak workshop registration',
        send_email=False,
        email=user.email,
        buyer_name=user.username,
        phone='',
        redirect_url=request.build_absolute_uri(reverse("payments:list"))
    )
    print(response)
    pid=response['payment_request']['id']
    bill=response['payment_request']['amount']
    pur=response['payment_request']['purpose']
    stat=response['payment_request']['status']
    settings.USER=user
    instamojo.objects.create(user=user,payment_id=pid,amount=bill,purpose=pur,status=stat)
    
    return HttpResponseRedirect(response['payment_request']['longurl'])

    # if a GET (or any other method) we'll create a blank form
    
    

    return render(request, 'pay.html', {})
    # return HttpResponse("Hello, world. You're at the API TEST index.")
from users.models import CustomUser
from django.http import HttpResponse
@login_required()
def list_payments(request):
    # Create a new Payment Request
    
    response = api.payment_requests_list()
    user=request.user
    insta=instamojo.objects.filter(user=user).order_by('-pk')[0]
    
    for response_status in response['payment_requests']:
        if response_status['id']==insta.payment_id:
            transactionStatus=response_status['status']
            
        

    
    if transactionStatus=='Completed':
        i=insta.payment_id
        ins=instamojo.objects.filter(payment_id=i).update(payment_done=True,status="successfull")
       # if not user.reg_amount and user.college=='1':
        #    update=CustomUser.objects.filter(username=user).update(reg_amount=True)
         #   subject = 'Your Payment'
          #  message='Hi ' + str(user.username)+' '+'your samyak id : '+str(user.samyak_id)+'  ,'+'you have been successfully registered to all events(*This doesn\'t include workshops)'
         #   send_mail(subject,message,'techsamyak19@gmail.com',[user.email],fail_silently=False)
           
          #  r=regPayment(student=user,reg_paymentType='4',token_id=i)
           # r.save()
           # return redirect(reverse('shopping_cart:update_records',
            #                kwargs={
             #                   'token': i,

              #              })
               #         )
 
        if user.profile.reg_paymethod=='1' : 
                return redirect(reverse('shopping_cart:update_records',
                            kwargs={
                                'token': i
                            })
                        )
        elif user.profile.reg_paymethod=='2':
            up=CustomUser.objects.filter(username=user).update(reg_amount=True)
            return redirect(reverse('shopping_cart:update_registration',
                    kwargs={
                        'token': i
                    })
                )
        elif user.profile.reg_paymethod=='3':
            up=CustomUser.objects.filter(username=user).update(reg_amount=True)
            subject = 'Your Payment'
            message='Hi ' + str(user.username)+' '+'your samyak id : '+str(user.samyak_id)+'  ,'+'you have been successfully registered to all events(*This doesn\'t include workshops)'
            send_mail(subject,message,'techsamyak19@gmail.com',[user.email],fail_silently=False)
            return redirect(reverse('shopping_cart:update_records',
                            kwargs={
                                'token': i,

                            })
                        )
            
    else:
        return redirect('newapp:events')
    
@login_required()
def registration_payments(request):

    user=request.user
    up=Profile.objects.filter(user=user).update(reg_paymethod='2')
    if not user.reg_amount:
        if user.college=='1':
            bill_amount =200
        else:
            bill_amount=500      
                                                                       
        # Create a new Payment Request
        response = api.payment_request_create(
            amount=str(bill_amount),
            purpose='Samyak Event registration',
            send_email=False,
            email=user.email,
            buyer_name=user.username,
            phone='',
            redirect_url=request.build_absolute_uri(reverse("payments:list"))
        )
        print(response)
        pid=response['payment_request']['id']
        bill=response['payment_request']['amount']
        pur=response['payment_request']['purpose']
        instamojo.objects.create(user=user,payment_id=pid,amount=bill,purpose=pur)
        up=Profile.objects.filter(user=user).update(reg_payment=True)
         
        
        return HttpResponseRedirect(response['payment_request']['longurl'])

    # if a GET (or any other method) we'll create a blank form
    else:
        return redirect('newapp:events')
    

    return render(request, 'pay.html', {})


