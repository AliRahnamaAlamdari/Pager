from django.shortcuts import render
from .models import Restaurant
from .serializers import RestaurantSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

class RestaurantAPIView(APIView):

    def get(self, request, Rest_id):
        restaurant = get_object_or_404(Restaurant, id=Rest_id)
        Restaurant_serializer = RestaurantSerializer(instance=restaurant)
        data = Restaurant_serializer.data
        return Response({'Restaurant': data})


    def post(self, request):
        rest_serializer = RestaurantSerializer(data=request.data)
        if rest_serializer.is_valid():
            rest_serializer.save()
            return Response({'message': 'restaurant added successfully!'})

        return Response({'message': rest_serializer.errors})

    def put(self, request, rest_id):
        restaurant = get_object_or_404(Restaurant, id=rest_id)
        rest_serializer = RestaurantSerializer(
            instance=restaurant, 
            data=request.data, 
            partial=True
        )

        if rest_serializer.is_valid():
            rest_serializer.save()
            return Response({'message': 'restaurant updated successfully!'})

        return Response({'message': rest_serializer.errors})
