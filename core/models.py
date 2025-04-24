from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# --- GESTOR PERSONALIZADO ---
class UsuarioManager(BaseUserManager):
    def create_user(self, correo_electronico, nombre, contraseña=None, **extra_fields):
        if not correo_electronico:
            raise ValueError('El correo electrónico es obligatorio')
        
        correo_electronico = self.normalize_email(correo_electronico)
        tipo_usuario = extra_fields.pop('tipo_usuario', 'cliente')  # lo extraemos de extra_fields

        user = self.model(
            correo_electronico=correo_electronico,
            nombre=nombre,
            tipo_usuario=tipo_usuario,
            **extra_fields
        )
        user.set_password(contraseña)
        user.save(using=self._db)
        return user

    def create_superuser(self, correo_electronico, nombre, contraseña=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('tipo_usuario', 'admin')  # aquí lo seteamos solo si no viene antes

        return self.create_user(correo_electronico, nombre, contraseña, **extra_fields)


# --- MODELO PERSONALIZADO DE USUARIO ---
class Usuario(AbstractBaseUser, PermissionsMixin):
    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField(unique=True)
    tipo_usuario = models.CharField(max_length=50, choices=[('cliente', 'Cliente'), ('admin', 'Admin')])
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'correo_electronico'
    REQUIRED_FIELDS = ['nombre', 'tipo_usuario']

    def __str__(self):
        return self.nombre

# --- CLIENTE (RELACIÓN UNO A UNO) ---
class Cliente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cliente: {self.usuario.nombre}"

# --- DIRECCIÓN ---
class Direccion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    calle = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.calle}, {self.ciudad}"

# --- INVENTARIO ---
class Inventario(models.Model):
    nombre_item = models.CharField(max_length=100)
    cantidad_disponible = models.IntegerField()

    def __str__(self):
        return self.nombre_item

# --- DESAYUNO ---
class Desayuno(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.FloatField()
    disponibilidad = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

# --- INGREDIENTE EN DESAYUNO ---
class IngredienteDesayuno(models.Model):
    desayuno = models.ForeignKey(Desayuno, on_delete=models.CASCADE, related_name='ingredientes')
    item = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    cantidad_necesaria = models.IntegerField()

# --- PEDIDO ---
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

# --- DETALLE DEL PEDIDO ---
class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    desayuno = models.ForeignKey(Desayuno, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

