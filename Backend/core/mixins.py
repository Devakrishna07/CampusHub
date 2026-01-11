# core/mixins.py
"""
Mixins add shared behavior to API views.
Avoids duplicate code across views.
"""

class RoleRequiredMixin:
    """
    Ensures a view can only be accessed by allowed roles.
    """
    allowed_roles = []

    def dispatch(self, request, *args, **kwargs):
        if request.user.role not in self.allowed_roles:
            raise PermissionError("You are not allowed to perform this action.")
        return super().dispatch(request, *args, **kwargs)
