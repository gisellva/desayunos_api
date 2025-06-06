from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Usuario, Cliente, Direccion, Inventario, Desayuno, IngredienteDesayuno, Pedido, DetallePedido
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from core.permissions import EsAdmin, EsCliente, EsAdminOReadOnly
from django.contrib.auth.hashers import make_password
from rest_framework import status

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
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.tipo_usuario == 'admin':
            return Pedido.objects.all()
        return Pedido.objects.filter(cliente__usuario=user)

class DetallePedidoViewSet(viewsets.ModelViewSet):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer
    permission_classes = [IsAuthenticated, EsCliente]

class MiPerfilView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        usuario = request.user
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)

    def patch(self, request):
        usuario = request.user
        data = request.data.copy()

        if 'password' in data and data['password']:
            data['password'] = make_password(data['password'])
        else:
            data.pop('password', None)

        serializer = UsuarioSerializer(usuario, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Perfil actualizado correctamente", "usuario": serializer.data})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

