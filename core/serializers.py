from rest_framework import serializers
from .models import Usuario, Cliente, Direccion, Inventario, Desayuno, IngredienteDesayuno, Pedido, DetallePedido

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        read_only_fields = ['usuario']  

    def validate(self, data):
        request_user = self.context['request'].user
        if request_user.tipo_usuario != "cliente":
            raise serializers.ValidationError("Solo los usuarios tipo 'cliente' pueden registrarse como clientes.")
        return data
    

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = '__all__'

class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = '__all__'

class DesayunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desayuno
        fields = '__all__'

class IngredienteDesayunoSerializer(serializers.ModelSerializer):
    desayuno_nombre = serializers.CharField(source='desayuno.nombre', read_only=True)
    item_nombre = serializers.CharField(source='item.nombre_item', read_only=True)

    class Meta:
        model = IngredienteDesayuno
        fields = ['id', 'cantidad_necesaria', 'desayuno', 'item', 'desayuno_nombre', 'item_nombre']


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'

class DetallePedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallePedido
        fields = '__all__'
