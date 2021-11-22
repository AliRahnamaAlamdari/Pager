from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import *


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('__all__')

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('__all__')

class AppMobileSignUpUserSerializer(serializers.ModelSerializer):
    role = serializers.IntegerField(default=1)
    class Meta:
        model = AppUser
        fields = ('"id", "username", "email", "password", "phone_number","role",')

    def create(self, validated_data):
        user = AppUser.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        Token.objects.get_or_create(user=user)
        user.save()
        return user

class AppMobileUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ('__all__')
