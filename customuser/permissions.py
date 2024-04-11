from rest_framework import permissions

from . import enums

class AppPermission(permissions.BasePermission):
    role = None
    
    def has_permission(self, request, view):
        user = request.user
        return bool(user.is_authenticated and self.role in user.roles)
    
class IsSuperAdmin(AppPermission):
    """Allows access only to super admin users."""
    message = "Only Super Admins are authorized to perform this task"
    role = "super_admin"
    
    
    

        
        
        
          
    