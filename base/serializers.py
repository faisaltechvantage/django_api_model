from rest_framework import serializers
from .models import User
from rest_framework.exceptions import ValidationError

# user serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

# user details update serializer
class UserDetailsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ("name", "age")