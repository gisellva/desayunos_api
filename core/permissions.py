from rest_framework.permissions import BasePermission, SAFE_METHODS

class EsAdmin(BasePermission):
   
    def has_permission(self, request, view):
        return hasattr(request.user, 'tipo_usuario') and request.user.tipo_usuario == 'admin'


class EsCliente(BasePermission):
   
    def has_permission(self, request, view):
        return hasattr(request.user, 'tipo_usuario') and request.user.tipo_usuario == 'cliente'


class EsAdminOReadOnly(BasePermission):
    
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return hasattr(request.user, 'tipo_usuario') and request.user.tipo_usuario == 'admin'
