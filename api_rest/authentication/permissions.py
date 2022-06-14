from re import X
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

class IsAuthenticatedOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        isAuth=IsAuthenticated()
        return request.method in SAFE_METHODS or isAuth.has_permission(request=request, view=view)