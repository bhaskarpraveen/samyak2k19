from django.conf.urls import url
from django.urls import include
from . import views as core_views
from .views import my_profile,logout_view
from django.contrib.auth import views as auth_views
app_name = 'accounts'

urlpatterns = [
	url(r'^profile/$', my_profile, name='my_profile'),
	url(r'^signup/$', core_views.signup, name='signup'),
	url(r'^logout/',logout_view,name='logout'),
	url( r'^login/$',auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    url(r'^password_reset/$',auth_views.PasswordResetView.as_view(template_name="registration/password_reset_form.html"), name='password_reset'),
    url(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
	auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), name='password_reset_confirm'),
    url(r'^reset/done/$',auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"), name='password_reset_complete'),
	url(r'^account_activation_sent/$', core_views.account_activation_sent, name='account_activation_sent'),
	url(r'^klaccount_activation_sent/$', core_views.klaccount_activation_sent, name='klaccount_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        core_views.activate, name='activate'),
	]

