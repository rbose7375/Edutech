from rest_framework import serializers
from .models import *

class ProductServicesCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductServicesCategory
        fields = '__all__'
        
class ProductServicesSerializer(serializers.ModelSerializer):
    category = ProductServicesCategorySerializer()
    class Meta:
        model = ProductServices
        fields = '__all__'