from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from shopping_cart.models import Order
from .models import Profile,CustomUser
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import CustomUserCreationForm
from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
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
from .forms import CustomUserCreationForm
from .tokens import account_activation_token
from .models import CustomUser
import sys
import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
from firebase_admin import db
from firebase_admin import auth
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

User = get_user_model()
cred=credentials.Certificate(
{
    "type": "service_account",
    "project_id": "androidmaterialdashboard",
    "private_key_id": "b1be709c109039f992fb86f93db08c400d59364c",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC7gx0+IzbxPPgo\nS651MQfVYSfzXta9vmV6X+8vi0xocC0d68whmvQE/uBOpCqBK8NMhR93w+vMx0Ng\nmTCsHS2qb3y2UE1I6k3E7HSzfuY9V8mf9MCuzTaDzb3D4GLyHl/Rtv/QIv9AXG0p\n9eUSFz7CxF+/2lTXFr0EfKNHyVEnCH7rY+jA1j3X8Hon1oFprP7yoRtp44/1G1H/\n+HL6fwCxWIxl5PRNu1X791YhTrn5L+TuM4FnGgG7ywBnyhiFHyB9fmzZBxbtWNeE\n2Okyb09qJuYEKUOWLaPrUsvEJpLSjH3hgaDnFPoX2UxQODt5iEIsz5lwi2FrhG0M\nH4zjb1nJAgMBAAECggEAF9Uxn472wgErkmWSIjON6RVM8F4ewaWkPMJaQor8Nm8B\nkQLCIohRGRxzEpPDkkDndP+bkQueGhw+iFXYLZwUzIuYiIya0hhzs4KRT6oipevV\nROclIWKUWfrJso5/zQHG0H8nswLrufi1aEaoa5z4PWWbvOUJcQAjHKGh2DMyhRkT\nsmP+CJvf8U65f1CXYbOJCbXb2GVyxMdtgE9u0C7lGbOFBc/zs4LvyqX8wnxj+cLQ\nf76vZr/OjQSsy9lfXrvPB5Uwuy+mlMzJiJY38d2kFc3VnEVkltdcEK1Di7m0GP5q\nElSklEv8nGZQHLG2xYdpOyHVAoeCsRGeBzaOHc7VnQKBgQDuSp3xGARemjluY5rG\nnsCsvR1DTUHdVGw8dKgtMfmYIdeCFORYrW3HJB2Q6zB+m0u4N/8WuwDIH0nD5rb/\n6rqCCCcRh4MorrF/k07WwRuONPTgNqqX+uUn6Pg1r1uoZD/zxHrufW53wJc04iTV\nq6s3a5z8sY7/JsmxGgOoxpsV7QKBgQDJcnHiOEz29C5AMEICMTqXXdkM4XAojzS/\n6gUeT4KoIw7n1sMEpIg/xYxTUpZ6DtBCXIjxo6IAbg1kqAoD8H6MuofCcpCbiRX8\n/BicmexQ3zTSb8Qdx+y5wEhetzXD5J0ipnFxnwooIIJgmwVQssYxCgyBpMMbEJql\nTPIy8pCXzQKBgGrHJuUdJQAbTbbojTeJdb8x8wXwfZ4nMWUZxS6TYUvJhl906ynN\ndQ6yYUlKCm4BOrnu5bCS1XPXiV9uZ/xfe3m/G3qgZaZ6OXF4WfCjkax0kHJULLdz\npvHuVCMCVCkt2vZpychKjpC8zUTWPTk99rgb0bnt+qzc/a4NgSxE6sO1AoGAcJry\nofvKufjAqczP+R2/nMEvBQ43fdSfLfAIsGrNpGMEgAACv2OhbdRlnmX6C3ygWZgU\nTM6lTgw2nF96Sb1zYAMcxEr6HpdAnUvmDhPUj1hV1JP5UpRg9WxQh/FtsnTmiWn0\n3AiEyu1xM8Mz82obc2okl4ucLFLZvzEF6gjBXrkCgYEAn+ErN69gqPvT3IiqTb/D\n11PKY9HIRo/NzkgObtu5eMlop7d1Q2ULTmDXLBO8zpV4QTf2/4CcmfWxmy1EeJCp\n6qKq3V/LvZTJSZ9XF7sD+cYkVCOgQm38Cvc3UixA2vXXjRVjNcYS8VJwufy+jJvy\nk9lw55A2aS4/w/OweT4Q7UQ=\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-4g9bx@androidmaterialdashboard.iam.gserviceaccount.com",
    "client_id": "110501182373995237225",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-4g9bx%40androidmaterialdashboard.iam.gserviceaccount.com"
})

firebase_admin.initialize_app(cred,{'databaseURL':'https://androidmaterialdashboard.firebaseio.com/',
'storageBucket':'androidmaterialdashboard.appspot.com'})

from .models import regPayment

@login_required()
def my_profile(request):
	my_user_profile = Profile.objects.filter(user=request.user).first()
	my_orders = Order.objects.filter(is_ordered=True, owner=my_user_profile)
	context = {
		'my_orders': my_orders

	}

	return render(request, "profile.html", context)


def logout_view(request):
    logout(request)
    return redirect(reverse('newapp:main'))

@login_required
def home(request):
    return render(request, 'home.html')

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
from django.utils.encoding import force_text

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
           # if clg=='1':
            
             #   send_mail(subject,message,'technical.samyak2k19@gmail.com',[str(mail)+"@kluniversity.in"],fail_silently=False)
            #    return redirect('accounts:klaccount_activation_sent')
            #else:
            user.email_user(subject, message)

            #user.is_active=True
            #Profile.email_confirmed = True
                   
            #login(request, user,backend='django.contrib.auth.backends.ModelBackend')

	
            return redirect('accounts:account_activation_sent')
            #return redirect('newapp:events')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'signup.html', {'form': form})


def klaccount_activation_sent(request):
    return render(request, 'klaccount_activation_sent.html',{})

def account_activation_sent(request):
    return render(request, 'account_activation_sent.html',{})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user,backend='django.contrib.auth.backends.ModelBackend')
        user=auth.create_user(
            email=user.email,
            password=user.password,
            email_verified=True
        )
        return redirect('newapp:events')
    else:
        return render(request, 'account_activation_invalid.html')


   
        
