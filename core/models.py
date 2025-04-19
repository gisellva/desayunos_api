from django.db import models


# Usuario general (base)
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=100)
    tipo_usuario = models.CharField(max_length=50)  # 'cliente' o 'admin'

    def __str__(self):
        return self.nombre

# Cliente hereda de Usuario (relación 1 a 1)
class Cliente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cliente: {self.usuario.nombre}"

# Dirección
class Direccion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    calle = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.calle}, {self.ciudad}"

# Inventario
class Inventario(models.Model):
    nombre_item = models.CharField(max_length=100)
    cantidad_disponible = models.IntegerField()

    def __str__(self):
        return self.nombre_item

# Desayuno
class Desayuno(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.FloatField()
    disponibilidad = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

# Ingrediente en un desayuno
class IngredienteDesayuno(models.Model):
    desayuno = models.ForeignKey(Desayuno, on_delete=models.CASCADE)
    item = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    cantidad_necesaria = models.IntegerField()

# Pedido
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    fecha_entrega = models.DateField()
    estado = models.CharField(max_length=50, choices=[
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En Proceso'),
        ('entregado', 'Entregado')
    ])
    total = models.FloatField()

    def __str__(self):
        return f"Pedido {self.id} - {self.estado}"

# Detalle del pedido
class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    desayuno = models.ForeignKey(Desayuno, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
