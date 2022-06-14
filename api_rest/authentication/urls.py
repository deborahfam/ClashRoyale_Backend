from django.urls import path
from .views import *

urlpatterns = [
    path('users/', ListCreateUserAPIView.as_view()),
    path('users/<pk>', RetrieveUpdateDestroyUserAPIView.as_view()),
    path('login/', LoginView.as_view(), name='auth_login'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
]