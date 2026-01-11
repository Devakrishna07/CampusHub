# core/permissions.py
"""
Reusable permission classes.
Applied to API views across the system.
"""

from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    """Allows access only to admins."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'ADMIN'


class IsJudge(BasePermission):
    """Allows only judges to update scores."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'JUDGE'


class HasEventAccess(BasePermission):
    """
    Ensures user is authorized for the specific event.
    Used for coordinators, judges, volunteers, evaluators.
    """
    def has_object_permission(self, request, view, obj):
        return obj in request.user.authorized_events.all()
