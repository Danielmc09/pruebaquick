from rest_framework import serializers

from .models import Clients

class ClientsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Clients
        exclude = ('last_login','is_superuser','is_staff','groups', 'user_permissions')

    def create(self, validate_data):
        user = Clients(**validate_data)
        user.set_password(validate_data['password'])
        user.save()
        return user