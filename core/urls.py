from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'direcciones', DireccionViewSet)
router.register(r'inventario', InventarioViewSet)
router.register(r'desayunos', DesayunoViewSet)
router.register(r'ingredientes-desayuno', IngredienteDesayunoViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'detalles-pedido', DetallePedidoViewSet)

urlpatterns = [
    path('', include(router.urls)), 
    
    path('mi-perfil/', MiPerfilView.as_view(), name='mi-perfil'),
]
