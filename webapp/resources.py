from import_export import resources
from .models import block

class courseResource(resources.ModelResource):
    class Meta:
        model = course
