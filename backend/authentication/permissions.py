from rest_framework.permissions import BasePermission


class FabricationPermission(BasePermission):
    def has_permission(self, request, view):
        # Logic to check if the user has the necessary permissions
        return True
        return request.user.user_type == "fabrication"


class SubAssemblyPermission(BasePermission):
    def has_permission(self, request, view):
        # Logic to check if the user has the necessary permissions
        return True
        return request.user.user_type == "sub-assembly"


class AssemblyPermission(BasePermission):
    def has_permission(self, request, view):
        # Logic to check if the user has the necessary permissions
        return True
        return request.user.user_type == "assembly"


class SuperFabricationPermission(BasePermission):
    def has_permission(self, request, view):
        return True
        return request.user.is_officer and request.user.user_type == "fabrication"


class SuperSubAssemblyPermission(BasePermission):
    def has_permission(self, request, view):
        return True
        return request.user.is_officer and request.user.user_type == "sub-assembly"


class SuperAssemblyPermission(BasePermission):
    def has_permission(self, request, view):
        return True
        return request.user.is_officer and request.user.user_type == "assembly"
