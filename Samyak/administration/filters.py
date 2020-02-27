from django.contrib.auth.models import User
import django_filters
from users.models import CustomUser,Profile
from products.models import Product
class UserFilter(django_filters.FilterSet):
    class Meta:
        model = CustomUser
        fields = [ 'samyak_id','email' ]
class ProfileFilter(django_filters.FilterSet):
    class Meta:
        model=Profile
        fields=['ebooks']
class ProductFilter(django_filters.FilterSet):
    class Meta:
        model=Product
        fields=['name']
