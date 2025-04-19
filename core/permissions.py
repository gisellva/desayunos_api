from rest_framework.permissions import BasePermission, SAFE_METHODS

class EsAdmin(BasePermission):
    """
    Permite el acceso solo a usuarios con tipo_usuario 'admin'.
    """
    def has_permission(self, request, view):
        return hasattr(request.user, 'tipo_usuario') and request.user.tipo_usuario == 'admin'


class EsCliente(BasePermission):
    """
    Permite el acceso solo a usuarios con tipo_usuario 'cliente'.
    """
    def has_permission(self, request, view):
        return hasattr(request.user, 'tipo_usuario') and request.user.tipo_usuario == 'cliente'


class EsAdminOReadOnly(BasePermission):
    """
    Permite solo lectura a cualquiera, pero escritura solo a admin.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return hasattr(request.user, 'tipo_usuario') and request.user.tipo_usuario == 'admin'
