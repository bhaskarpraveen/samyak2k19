from django.contrib import admin

from .models import OrderItem, Order, Transaction

admin.site.register(OrderItem)
admin.site.register(Order)


class TransactionAdmin(admin.ModelAdmin):
    model = Transaction
    list_display = ['profile','token',]
    search_fields=('profile__user__username','profile__user__samyak_id','token','order_id',)
    
    
    
     
admin.site.register(Transaction,TransactionAdmin)