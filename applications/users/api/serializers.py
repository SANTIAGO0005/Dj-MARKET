from rest_framework import serializers
from ...users.models import User

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
   pass

class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email','full_name')



