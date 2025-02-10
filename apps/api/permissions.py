from rest_framework.permissions import BasePermission


class AccountOwner(BasePermission):
    """
    Custom permission to only allow access to the account owner.
    """

    def has_permission(self, request, view):
        """
        Return True if the selected user matches the request user, else False.
        """
        try:
            return request.user.get_selected() == request.user
        except AttributeError:
            return False
