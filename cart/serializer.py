from rest_framework import serializers
from .models import *
from services.serializer import *
from users.serializer import *

class FavoriteListSerializer(serializers.ModelSerializer):
    product = ProductServicesSerializer()
    user = UserSerializer()
    class Meta:
        model = FavoriteList
        fields = '__all__'
        
class BookClassSerializer(serializers.ModelSerializer):
    product = ProductServicesSerializer()
    user = UserSerializer()
    class Meta:
        model = BookClass
        fields = '__all__'
        