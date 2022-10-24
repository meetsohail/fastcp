from rest_framework import permissions
from django.conf import settings

class CreateUserPermit(permissions.BasePermission):

    edit_methods = ("POST", "GET")

    def has_permission(self, request, view):
        if request.GET.get('permit'):
            if request.GET.get('permit') is settings.PERMIT:
                return True
        return False