from django.db.models import fields
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Clients

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ['email', 'first_name' ]

class ClientsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Clients
        exclude = ('last_login','is_superuser','is_staff','groups', 'user_permissions')

    def create(self, validate_data):
        user = Clients(**validate_data)
        user.set_password(validate_data['password'])
        user.save()
        return user


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ['email', 'password']

    def create(self, validate_data):
        user = Clients(**validate_data)
        user.set_password(validate_data['password'])
        user.save()
        return user
    

