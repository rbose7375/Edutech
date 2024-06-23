from rest_framework import serializers
from .models import User
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    
    def get_token(self, obj):
        token = Token.objects.get_or_create(user = obj)[0]
        return token.key
    class Meta:
        model = User
        fields = ['email','first_name', 'mobile', 'gender','birth_date','avatar','token']