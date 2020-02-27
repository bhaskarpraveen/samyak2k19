from django.contrib import admin
from users.models import regPayment
from .models import evePayment
# Register your models here.



class regPaymentAdmin(admin.ModelAdmin):
    model = regPayment
    list_display = ['student','reg_paymentType','token_id']
    search_fields=('student','token_id')
admin.site.register(regPayment,regPaymentAdmin)
class evePaymentAdmin(admin.ModelAdmin):
    model = regPayment
    list_display = ['name','user_id','idnumber']
    search_fields=('name__name','user_id','idnumber')
admin.site.register(evePayment,evePaymentAdmin)



