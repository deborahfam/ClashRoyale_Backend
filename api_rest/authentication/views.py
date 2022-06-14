from .models import *
from api_rest.pagination import CRPagination
from api_rest.serializers import get_serializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
# Create your views here.

class ListCreateUserAPIView(ListCreateAPIView):
    serializer_class = get_serializer(User)
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]
    pagination_class = CRPagination
    # filter_backends = (filters.DjangoFilterBackend,)
    # filterset_class = MovieFilter

class RetrieveUpdateDestroyUserAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = get_serializer(User)
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]

class LoginView(APIView):
    @method_decorator(csrf_exempt)  
    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return Response(status=status.HTTP_200_OK)

        return Response(
            status=status.HTTP_404_NOT_FOUND)

class LogoutView(APIView):
    @method_decorator(csrf_exempt)  
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)