from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Usuario, Cliente, Direccion, Inventario, Desayuno, IngredienteDesayuno, Pedido, DetallePedido
from .serializers import *
from core.permissions import EsAdmin, EsCliente, EsAdminOReadOnly

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated, EsCliente]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class DireccionViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer
    permission_classes = [IsAuthenticated, EsCliente]

class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer
    permission_classes = [IsAuthenticated, EsAdmin]

class DesayunoViewSet(viewsets.ModelViewSet):
    queryset = Desayuno.objects.all()
    serializer_class = DesayunoSerializer
    permission_classes = [EsAdminOReadOnly]
class IngredienteDesayunoViewSet(viewsets.ModelViewSet):
    queryset = IngredienteDesayuno.objects.all()
    serializer_class = IngredienteDesayunoSerializer
    permission_classes = [IsAuthenticated, EsAdmin]

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [IsAuthenticated, EsCliente]

class DetallePedidoViewSet(viewsets.ModelViewSet):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer
    permission_classes = [IsAuthenticated, EsCliente]
