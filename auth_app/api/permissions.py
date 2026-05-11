from rest_framework.permissions import BasePermission

class IsQuizlyUser(BasePermission):
    """
    Custom permission to only allow users of the Quizly app to access certain views.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated and belongs to the Quizly app
        return request.user and request.user.is_authenticated 
    
    def has_object_permission(self, request, view, obj):
        # Object-level permission: Only allow access if the user is the owner of the object
        return obj.user == request.user