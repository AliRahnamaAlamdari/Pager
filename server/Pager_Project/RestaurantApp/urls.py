from django.urls import path

from MobileApp.views import *
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('login/', view=obtain_auth_token),
]