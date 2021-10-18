from rest_framework import serializers

from .models import Bills

class BillsSerializers(serializers.ModelSerializer):
    #content = ProductsSerializers(many=True, read_only=True)
    class Meta:
        model = Bills
        fields = '__all__'