from pickle import TRUE
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=50, default='', unique=TRUE)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50, default='')
    role = models.ForeignKey(
        'Roles',
        on_delete=models.CASCADE,
        null=True,
    )
    # def get_form(self, request, obj=None, **kwargs):
    #     # Get form from original UserAdmin.
    #     form = super(abs, self).get_form(request, obj, **kwargs)
    #     if 'user_permissions' in form.base_fields:
    #         permissions = form.base_fields['user_permissions']
    #         permissions.queryset = {}
    #     return form
    
class Scopes(models.Model):
    SC_name = models.CharField(max_length=50)

class Roles(models.Model):
    R_name = models.CharField(max_length=50)
class User_Scopes(models.Model):
    SC_ID= models.ForeignKey(
        'Scopes',
        on_delete=models.CASCADE,
    )
    U_ID= models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
    )

class Roles_Scopes(models.Model):
    SC_ID= models.ForeignKey(
        'Scopes',
        on_delete=models.CASCADE,
    )
    R_ID= models.ForeignKey(
        'Roles',
        on_delete=models.CASCADE,
    )

class OAuth(models.Model):
    OA_token = models.CharField(max_length=32)
    OA_date = models.DateField()
