from django.contrib import admin
from django.contrib.sites.models import Site
# Register your models here.
from .models import Profile



from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ['user']
    search_fields=('user__username','user__samyak_id','user__email','user__id_number') 
admin.site.register(Profile,ProfileAdmin)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['samyak_id','created','fullname','phonenumber','email','gender', 'username','reg_amount','college','college_name','id_number','is_amb','can_amb']
    search_fields=('samyak_id','username','id_number')
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(Site)

class SiteAdmin(admin.ModelAdmin):
    fields = ('id', 'name', 'domain')
    readonly_fields = ('id',)
    list_display = ('id', 'name', 'domain')
    list_display_links = ('name',)
    search_fields = ('name', 'domain')
admin.site.register(Site, SiteAdmin)

