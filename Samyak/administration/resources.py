from import_export import resources
from users.models import CustomUser
class PersonResource(resources.ModelResource):
    class Meta:
        model = CustomUser
