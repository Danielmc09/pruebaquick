from import_export import resources
from .models import Clients

class ClientsResource(resources.ModelResource):
    class Meta:
        model = Clients