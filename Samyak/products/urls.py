from django.conf.urls import url

from .views import product_list,nonTechnical,workshops,paperpresen,departmentevents,literaryEvents

app_name = 'products'

urlpatterns = [
    url(r'^themebased', product_list, name='product-list'),
    url(r'^nontechnical',nonTechnical,name='nonTechnical'),
    url(r'^workshops',workshops,name='workshops'),
    url(r'^paperpresentation',paperpresen,name='paperpresen'),
    url(r'^departmentevents',departmentevents,name='departmentevents'),
    url(r'literaryevents',literaryEvents,name='literaryevents')
]
