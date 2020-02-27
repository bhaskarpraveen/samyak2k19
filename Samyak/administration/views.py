
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from shopping_cart.models import Order
from users.models import Profile,CustomUser
from django.shortcuts import render, redirect
from django.urls import reverse

from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from users.tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from users.forms import CustomUserCreationForm
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# Create your views here.
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('newapp:main')
@staff_member_required
def admin_main(request):
    return render(request,'adminMain.html',{})
@staff_member_required
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


@staff_member_required
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            clg=form.cleaned_data['college']
            mail=form.cleaned_data['id_number']
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
           # user.is_active=True
           # Profile.email_confirmed = True
           # user.save()

            #login(request, user,backend='django.contrib.auth.backends.ModelBackend')
            #if clg=='1':
            
             #   send_mail(subject,message,'techsamyak19@gmail.com',[str(mail)+"@kluniversity.in"],fail_silently=False)
              #  return redirect('accounts:klaccount_activation_sent')
         
            user.email_user(subject, message)

            return redirect('administration:admin_main')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration.html', {'form': form})


def account_activation_sent(request):
    return render(request, 'account_activation_sent.html')
from .filters import UserFilter
@staff_member_required
def allUsers(request):
    us=CustomUser.objects.all()
    user_filter = UserFilter(request.GET)
    return render(request,'allusers.html',{'users':us,'filter': user_filter})
from users.forms import Payment
from users.models import CustomUser
from django.views.generic.edit import FormView
from django.core.mail import send_mail

@staff_member_required
@staff_member_required
def regPayments(request):
    if request.method=='POST':
        form=Payment(request.POST)
        if form.is_valid():
            done=form.cleaned_data['student']
            cash=form.cleaned_data['Amount']
            try:
                c=CustomUser.objects.get(samyak_id=done)
            except:
                return HttpResponse('Invalid samyakid please check')
              
            up=CustomUser.objects.filter(samyak_id=done).update(reg_amount=True)
            subject = 'Your Payment'
            message='Hi ' + str(c.username)+' '+'your samyak id : '+str(c.samyak_id)+'  ,'+'you have been successfully registered to all events(*This doesn\'t include workshops)'
            send_mail(subject,message,'techsamyak19@gmail.com',[c.email],fail_silently=False)
            form.save()
            return HttpResponse('success')
            
    else:
        form=Payment()
    return render(request,'regamount.html',{'form':form})

from .filters import ProfileFilter,ProductFilter
from products.models import Product
@staff_member_required
def eventsdb(request):
    us=Profile.objects.all()
    product_filter = ProfileFilter(request.GET)
    return render(request,'eventdb.html',{'p':us,'filter':product_filter})
@staff_member_required
def eventsadmin(request):
    return render(request,'eventsadmin.html',{})
from .forms import offPayments
from django.core.mail import send_mail
@staff_member_required
def eventpayments(request):
    if request.method=='POST':
        form=offPayments(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            us=form.cleaned_data['user_id']
        
            prod=Product.objects.get(name=name)
            obj=prod.price
            lim=prod.limit
            num=Profile.objects.filter(ebooks=name).count()
            
            cus=CustomUser.objects.get(samyak_id=us)
            c=Profile.objects.get(user=cus)
            check=Profile.objects.filter(user=cus,ebooks=name)
            if check:
                return HttpResponse('already registered')
            c.ebooks.add(name)
            num1=Profile.objects.filter(ebooks=name).count()
            n=Product.objects.filter(name=prod).update(numberofreg=num1)
            subject='your payment'
            
            message='Hi '+str(cus.username)+'  '+'your samyak id :'+ str(cus.samyak_id) +'   ,'+ 'you have been successfully registered to '+str(name)
            send_mail(subject,message,'techsamyak19@gmail.com',[cus.email],fail_silently=False)
            form.save()
            return HttpResponse('success')
            
    else:
        form=offPayments()
    return render(request,'eventpayments.html',{'form':form})


from django.http import HttpResponse
from .resources import PersonResource
@staff_member_required
def export(request):
    person_resource = PersonResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="persons.xls"'
    return response

@staff_member_required
def update(request):
    pro=Product.objects.all()
    for p in pro:
        c=Profile.objects.filter(ebooks=p).count()
        Product.objects.filter(name=p).update(numberofreg=c)
        if c>=p.limit:
            u=Product.objects.filter(name=p).update(limit_exceeded=True)
        else:
            u=Product.objects.filter(name=p).update(limit_exceeded=False)
    
        n=Product.objects.filter(name=p).update(numberofreg=c)
    return HttpResponse('success')

from .forms import activate
@staff_member_required
def superactivate(request):
    if request.method=='POST':
        form=activate(request.POST)
        if form.is_valid():
            num=form.cleaned_data['i']
            s=CustomUser.objects.get(samyak_id=num)
            s.is_active = True
            s.profile.email_confirmed = True
            s.save()
            return HttpResponse('Done')
    else:
        form=activate()
    return render(request,'superactivate.html',{'form':form})



from .forms import *
from products.models import  Attendence
def attendence(request,event):
    if request.user.groups.filter(name=event).exists() or request.user.is_superuser:
        if request.method=='POST':
            form=AttendenceForm(request.POST)
            if form.is_valid():
                student=form.cleaned_data['samyak_id']
                eve=Product.objects.get(name=event)
                st=CustomUser.objects.get(samyak_id=student)
                v1=st.reg_amount
                v2=Profile.objects.filter(user=st,ebooks=eve)
                if not v1 and not v2:
                    return HttpResponse('Not registered for the event')
                att=Attendence.objects.get(event_name=eve)
                att.attendees.add(st)
                att.save()
                return HttpResponse('Done')
               
                return HttpResponse('Enter valid details')
        else:
            form=AttendenceForm()
        return render(request,'attendenceform.html',{'form':form})
    else:
        return HttpResponse('No access')
def eventattendence(request,event):
    if  request.user.groups.filter(name=event).exists() or request.user.is_superuser:
       
         pro=Product.objects.get(name=event)
         ty=pro.eventType
         reg=''
         total=Profile.objects.filter(ebooks=pro).count()
         tot=Profile.objects.filter(ebooks=pro)
         
         if ty !='W':
             reg=CustomUser.objects.filter(reg_amount=True)
             print(reg)
             c=CustomUser.objects.filter(reg_amount=True).count()
             total=total+c



         
         return render(request,'eventattendence.html',{'user':tot,'num':total,'reg':reg}) 
       
           
    else:
        return HttpResponse('No access')

def attendenceadmin(request,event):
    if  request.user.groups.filter(name=event).exists() or request.user.is_superuser:
        return render(request,'attendenceadmin.html',{'eve':event})
    else :
        return HttpResponse('No access')
from random import randint
from random import randint
@staff_member_required 
def change(request):
    prod=Product.objects.all()
    for pro in prod:
        p=Product.objects.get(name=pro)
        t=p.limit
        r=p.numberofreg
        a=t-r
        if a > 25:
            a=randint(10,25)
        print(pro)
     
        Product.objects.filter(name=pro).update(display=a)


    return HttpResponse('Done :)')
