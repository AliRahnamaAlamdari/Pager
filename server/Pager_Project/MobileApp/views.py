from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from django.views.decorators.csrf import csrf_exempt , csrf_protect
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .models import *
from .serializers import AppMobileSignUpUserSerializer , OrderSerializer , AppMobileUserSerializer , OrderItemSerializer
from RestaurantApp.serializers import FoodSerializer , FoodGroupSerializer

class CustomObtainAuthToken(ObtainAuthToken):
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                       context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
        })

class SignUpMobileUser(APIView):

    @csrf_exempt
    def post(self, request):
        serializer = AppMobileSignUpUserSerializer(data=request.data)
        
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(data={"message": "created"})
            except Exception as e:
                return Response(data={"message": serializer.errors})
        return Response(serializer.errors)

class UsersAPIView(APIView):
    def get(self,request,user_id):
        user = get_object_or_404(AppUser,pk=user_id)
        user_serializer = AppMobileUserSerializer(instance=user)
        data = user_serializer.data
        return Response(
            {
                "info" : data
            }
        )





class AddOrderAPIView(APIView):
    def post(self, request):
        order_serializer = OrderSerializer(data=request.data)
        if order_serializer.is_valid():
            order_serializer.save()
            return Response({'message': 'order added successfully!'})

        return Response({'message': order_serializer.errors})

class OrderAPIView(APIView):
    def get(self, request, order_id):
        order = get_object_or_404(Orders, id=order_id)
        order_serializer = OrderSerializer(instance=order)
        data = order_serializer.data
        return Response({'order': data})

    def put(self, request, order_id):
        order = get_object_or_404(Orders, id=order_id)
        order_serializer = OrderSerializer(
            instance=order, 
            data=request.data, 
            partial=True
        )

        if order_serializer.is_valid():
            order_serializer.save()
            return Response({'message': 'Order updated successfully!'})

        return Response({'message': order_serializer.errors})

class OrdersOfUser(APIView):
    def get(self,request,state, user_id):
        if state == "active":
            return Response({"orders" : OrderSerializer(instance=Orders.objects.filter(User__pk=user_id).filter(is_prepaerd= False) , many =True).data})
        else:
            return Response({"orders" : OrderSerializer(instance=Orders.objects.filter(User__pk=user_id).filter(is_prepaerd=True) , many =True).data})

class OrderItemsOfOrder(APIView):
    def get(self, request, order_id):
        return Response({"orderItems" : OrderItemSerializer(instance=OrderItem.objects.filter(Order=order_id) , many =True).data})


class FoodAPIview(APIView):
    def get(self,request , food_id):
        return Response({"food" : FoodSerializer(FoodItem.objects.get(pk = food_id)).data})


class FoodGroupAPIview(APIView):
    def get(self,request , foodGP_id):
        return Response({"foodGP" : FoodGroupSerializer(FoodGroup.objects.get(pk = foodGP_id)).data})
