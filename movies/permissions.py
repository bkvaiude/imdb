from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow Admin to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS and request.user.is_anonymous()==False:#no guest
            return True

        # Instance must have an attribute named `admin`.
        return request.user.is_staff == True
