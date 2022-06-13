from http.client import ImproperConnectionState
from sre_constants import SUCCESS
from django.http.response import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import *
import json
from api_rest.pagination import CRPagination
from api_rest.serializers import get_serializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
# Create your views here.


class ListCreateUserAPIView(ListCreateAPIView):
    serializer_class = get_serializer(User)
    queryset = User.objects.all()
    # permission_classes = [IsAuthenticated]
    pagination_class = CRPagination
    # filter_backends = (filters.DjangoFilterBackend,)
    # filterset_class = MovieFilter

    @method_decorator(csrf_exempt)
    def perform_create(self, serializer):
        serializer.save()

class RetrieveUpdateDestroyUserAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = get_serializer(User)
    queryset = User.objects.all()
    @method_decorator(csrf_exempt)
    def __nada():
        pass
    # permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

# class UserView(View):    
#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)
    
#     def get(self,request):
#         all = list(User.objects.values())
#         if len(all)>0:
#             data = {'message': "Success", 'Users': all}
#         else:
#             data = {'message': "Fail"}
#         return JsonResponse(data)
    
#     def post(self,request):
#         jd = json.loads(request.body)
#         User.objects.create(
#             username=jd['username'], 
#             email=jd['email'], 
#             password=jd['password'], 
#             role=jd['role']
#         )
#         data={'message':'Success'}
#         return JsonResponse(data)
    
#     def put(self,request,id):
#         jd = json.loads(request.body)
#         all = list(User.objects.filter(id=id).values())
#         if len(all)>0:
#             elem = User.objects.get(id=id)
#             elem.username=jd['username']
#             elem.email=jd['email']
#             elem.password=jd['password']
#             elem.role=jd['role']
#             elem.save()
#             data = {'message': "Success"}
#         else:
#             data = {'message': "Fail"}
#         return JsonResponse(data)

#     def delete(self,request,id):
#         all = list(User.objects.filter(id=id).values())
#         if len(all)>0:
#             User.objects.filter(id=id).delete()
#             data = {'message': "Success"}
#         else:
#             data = {'message': "Fail"}
#         return JsonResponse(data)

class ScopesManagement(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request):
        all = list(Scopes.objects.values())
        if len(all)>0:
            data = {'message': "Success", 'Scopes': all}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)
    
    def post(self,request):
        jd = json.loads(request.body)
        Scopes.objects.create(
            SC_name=jd['SC_name']
        )
        data={'message':'Success'}
        return JsonResponse(data)
    
    def put(self,request,id):
        jd = json.loads(request.body)
        all = list(Scopes.objects.filter(id=id).values())
        if len(all)>0:
            elem = Scopes.objects.get(id=id)
            elem.SC_name=jd['SC_name']
            elem.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)

    def delete(self,request,id):
        all = list(Scopes.objects.filter(id=id).values())
        if len(all)>0:
            Scopes.objects.filter(id=id).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)

class User_Scopes(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request):
        all = list(User_Scopes.objects.values())
        if len(all)>0:
            data = {'message': "Success", 'User_Scopes': all}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)
    
    def post(self,request):
        jd = json.loads(request.body)
        User_Scopes.objects.create(
            SC_ID=jd['SC_ID'], 
            U_ID=jd['U_ID']
        )
        data={'message':'Success'}
        return JsonResponse(data)
    
    def put(self,request,id):
        jd = json.loads(request.body)
        all = list(User_Scopes.objects.filter(id=id).values())
        if len(all)>0:
            elem = User_Scopes.objects.get(id=id)
            elem.SC_ID=jd['SC_ID']
            elem.U_ID=jd['U_ID']
            elem.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)

    def delete(self,request,id):
        all = list(User_Scopes.objects.filter(id=id).values())
        if len(all)>0:
            User_Scopes.objects.filter(id=id).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)
class Roles_Scopes(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request):
        all = list(Roles_Scopes.objects.values())
        if len(all)>0:
            data = {'message': "Success", 'Roles_Scopes': all}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)
    
    def post(self,request):
        jd = json.loads(request.body)
        Roles_Scopes.objects.create(
            SC_ID=jd['SC_ID'], 
            R_ID=jd['R_ID']
        )
        data={'message':'Success'}
        return JsonResponse(data)
    
    def put(self,request,id):
        jd = json.loads(request.body)
        all = list(Roles_Scopes.objects.filter(id=id).values())
        if len(all)>0:
            elem = Roles_Scopes.objects.get(id=id)
            elem.SC_ID=jd['SC_ID']
            elem.R_ID=jd['R_ID']
            elem.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)

    def delete(self,request,id):
        all = list(Roles_Scopes.objects.filter(id=id).values())
        if len(all)>0:
            Roles_Scopes.objects.filter(id=id).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)
class RolesManagement(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request):
        all = list(Roles.objects.values())
        if len(all)>0:
            data = {'message': "Success", 'Roles': all}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)
    
    def post(self,request):
        jd = json.loads(request.body)
        Roles.objects.create(
            R_name=jd['R_name']
        )
        data={'message':'Success'}
        return JsonResponse(data)
    
    def put(self,request,id):
        jd = json.loads(request.body)
        all = list(Roles.objects.filter(id=id).values())
        if len(all)>0:
            elem = Roles.objects.get(id=id)
            elem.R_name=jd['R_name']
            elem.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)

    def delete(self,request,id):
        all = list(Roles.objects.filter(id=id).values())
        if len(all)>0:
            Roles.objects.filter(id=id).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)
class OAuth(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request):
        all = list(OAuth.objects.values())
        if len(all)>0:
            data = {'message': "Success", 'OAuths': all}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)
    
    def post(self,request):
        jd = json.loads(request.body)
        OAuth.objects.create(
            OA_token=jd['OA_token'], 
            OA_date=jd['OA_date']
        )
        data={'message':'Success'}
        return JsonResponse(data)
    
    def put(self,request,id):
        jd = json.loads(request.body)
        all = list(OAuth.objects.filter(id=id).values())
        if len(all)>0:
            elem = OAuth.objects.get(id=id)
            elem.OA_token=jd['OA_token']
            elem.OA_date=jd['OA_date']
            elem.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)

    def delete(self,request,id):
        all = list(OAuth.objects.filter(id=id).values())
        if len(all)>0:
            OAuth.objects.filter(id=id).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)