from rest_framework import serializers

from .models import Products

class ProductSerializer(serializers.ModelSerializer):
    #content = ProductsSerializers(many=True, read_only=True)
    class Meta:
        model = Products
        fields = '__all__'