from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import re_path
from django.views.static import serve
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^administration/',include('administration.urls',namespace='administration')),
    url(r'^profiles/', include('users.urls', namespace='accounts')),
    url(r'^profiles/',include('django.contrib.auth.urls')),
    url(r'events/', include('products.urls', namespace='products')),
    url(r'^cart/', include('shopping_cart.urls', namespace='shopping_cart')),
    url(r'^paytm/',include('paytm.urls',namespace='paytm')),
    url(r'^campus-ambassador/', include('home.urls',namespace='home')),
    url(r'^payments/', include("apitest.urls",namespace='payments')),
    url(r'^', include('newapp.urls',namespace='newapp')),
    
    #re_path(r'^paytm/', include('paytm.urls')),

]

if not settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
        url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    ]
