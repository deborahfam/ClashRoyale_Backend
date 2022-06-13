from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Scopes)
admin.site.register(Roles)
admin.site.register(User_Scopes)
admin.site.register(Roles_Scopes)
admin.site.register(OAuth)