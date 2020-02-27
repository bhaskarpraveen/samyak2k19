from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from . import views
from administration.views import eventsadmin,eventsdb,eventsadmin,eventpayments,eventattendence,attendence,attendenceadmin
app_name='newapp'
urlpatterns = [
	path('dashboard/',dash,name='dash'),
        path('accomodation/',accomodation,name='accomodation'),
	#path('accomodationpay/',accomodationpay,name='accomodationpay'),
        path('mycertificates/',mycertificates,name='mycertificates'),
        path('prototypeexpo/',prototypeexpo,name='prototypeexpo'),
        path('posterpresentation/',posterpresentation,name='posterpresentation'),
        path('eventattendance/<str:event>/',eventattendence,name='eventattendence'),
        path('attendance/<str:event>',attendence,name='attendence'),
	path('attendanceadmin/<str:event>/',attendenceadmin,name='attendenceadmin'),
	path('eventsadministration/',eventsadmin,name='eventsadmin'),
	path('regadministration/',eventsdb,name='eventsdb'),
	path('eventpayments/',eventpayments,name='eventpayments'),
	path('events/',events,name='events'),
	path('pretechnical/',pretechnical,name='pretechnical'),
	path('sponsors/',sponsors,name='sponsors'),
	path('gallery/',gallery,name='gallery'),
	path('about/',about,name='about'),
	path('contact/',contact,name='contact'),
	path('proshow/',proshow,name='proshow'),
	path('success', views.success, name = 'success'),
	path('explore-17/',views.explore_17,name='explore_17'),
	path('explore-18/',views.explore_18,name='explore_18'),
	path('explore-19/',views.explore_19,name='explore_19'),
	path('team/',team,name='team'),
	path('<int:pk>/edit/',
         ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/',
         ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/delete/',
         ArticleDeleteView.as_view(), name='article_delete'),
    path('new/', ArticleCreateView.as_view(), name='article_new'),
    path('all/', ArticleListView.as_view(), name='article_list'),
	path('',main,name='main'),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
