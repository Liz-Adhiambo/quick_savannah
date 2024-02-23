from rest_framework import serializers
from .models import Customer, Order
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)

        return user

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('__all__')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('__all__')
class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()



    
