from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="Admin").exists()


class IsAdminOrReadOnly(BasePermission):
    """
    Admin → full access
    Analyst → read-only access
    """

    def has_permission(self, request, view):
        # Read-only access for authenticated users (Analyst)
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated

        # Write access only for Admin
        return request.user.groups.filter(name="Admin").exists()

class AnalystReadOnly(BasePermission):
    """
    Analyst: Read-only access
    Admin: Full access
    """

    def has_permission(self, request, view):
        user = request.user

        if not user or not user.is_authenticated:
            return False

        # Read-only → Analyst + Admin
        if request.method in SAFE_METHODS:
            return (
                user.groups.filter(name='Analyst').exists() or
                user.groups.filter(name='Admin').exists()
            )

        # Write access → Admin only
        return user.groups.filter(name='Admin').exists()