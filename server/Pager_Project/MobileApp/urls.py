from django.urls import path

from MobileApp.views import *
from RestaurantApp.views import RestaurantAPIView
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('order/add/', AddOrderAPIView.as_view()),
    path('order/<int:order_id>/', OrderAPIView.as_view()),
    path('orderItems/<int:order_id>/', OrderItemsOfOrder.as_view()),
    path('orders/<str:state>/<int:user_id>/', OrdersOfUser.as_view()),
    path('Restaurant/<int:Rest_id>/', RestaurantAPIView.as_view()),
    path('food/<int:food_id>/', FoodAPIview.as_view()),
    path('foodGroup/<int:foodGP_id>/', FoodGroupAPIview.as_view()),
    path('userinfo/<int:user_id>/', UsersAPIView.as_view()),
    path('login/', view=CustomObtainAuthToken.as_view()),
    path('signup/', view=SignUpMobileUser.as_view()),
]