from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        # if the user is staff, they can do anything
        if request.user.is_staff:
            return True

        # otherwise Write permissions are only allowed to the owner of the item.
        return obj.registered_by == request.user