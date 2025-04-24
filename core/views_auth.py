from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from core.models import Usuario
from core.serializers import UsuarioSerializer
from core.permissions import EsAdmin
from rest_framework.permissions import IsAuthenticated

class CustomLoginView(APIView):
    def post(self, request):
        correo = request.data.get("username")
        contraseña = request.data.get("password")

        try:
            usuario = Usuario.objects.get(correo_electronico=correo)
        except Usuario.DoesNotExist:
            return Response({"detail": "Usuario no encontrado"}, status=status.HTTP_401_UNAUTHORIZED)

       
        if not usuario.check_password(contraseña):
            return Response({"detail": "Contraseña incorrecta"}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(usuario)

        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "usuario_id": usuario.id,
            "nombre": usuario.nombre,
            "tipo_usuario": usuario.tipo_usuario
        })

class RegistroClienteView(APIView):
    def post(self, request):
        data = request.data.copy()
        data['tipo_usuario'] = 'cliente'

        serializer = UsuarioSerializer(data=data)
        if serializer.is_valid():
            usuario = serializer.save()
            usuario.set_password(data['password'])  
            usuario.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegistroAdminView(APIView):
    permission_classes = [IsAuthenticated, EsAdmin]

    def post(self, request):
        data = request.data.copy()
        data['tipo_usuario'] = 'admin'

        serializer = UsuarioSerializer(data=data)
        if serializer.is_valid():
            usuario = serializer.save()
            usuario.set_password(data['password'])  
            usuario.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
