from rest_framework import permissions

class IsOwnerOrStaff(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.registered_by == request.user or request.user.is_staff