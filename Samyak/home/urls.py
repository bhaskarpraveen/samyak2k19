from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
app_name='home'
from .views import (
    create_book_normal,
    create_book_model_form,
    create_book_with_authors,
    BookListView,
)

urlpatterns = [
	
	
    re_path(r'^', create_book_with_authors, name='create_book_with_authors'),
    re_path(r'^book/list', BookListView.as_view(), name='book_list'),
    
	
]
if settings.DEBUG:
  
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





