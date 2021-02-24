from rest_framework import permissions

class HasPerm(permissions.BasePermission):
    def has_permission(self, request, view):
        return super().has_permission(request, view)

class IsOwnProfileOrAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        is_admin = super().has_permission(request, view)
        return obj.user == request.user or is_admin

class IsOwnProfileOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile == request.user.profile