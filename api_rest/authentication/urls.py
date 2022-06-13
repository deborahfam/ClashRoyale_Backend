from django.urls import path
from .views import *

urlpatterns = [
    path('users/', ListCreateUserAPIView.as_view()),
    path('users/<pk>', RetrieveUpdateDestroyUserAPIView.as_view()),
    path('scopesmanagements/', ScopesManagement.as_view()),
    path('scopesmanagements/<int:id>', ScopesManagement.as_view()),
    path('user_scopes/', User_Scopes.as_view()),
    path('user_scopes/<int:id>', User_Scopes.as_view()),
    path('roles_scopes/', Roles_Scopes.as_view()),
    path('roles_scopes/<int:id>', Roles_Scopes.as_view()),
    path('rolesmanagements/', RolesManagement.as_view()),
    path('rolesmanagements/<int:id>', RolesManagement.as_view()),
    path('oauths/', OAuth.as_view()),
    path('oauths/<int:id>', OAuth.as_view()),
]