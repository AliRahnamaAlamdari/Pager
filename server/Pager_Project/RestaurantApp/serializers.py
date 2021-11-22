from rest_framework import serializers

from .models import *




class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('__all__')

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = ('__all__')

class FoodGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodGroup
        fields = ('__all__')