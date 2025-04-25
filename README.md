# 🥞 API Desayunos Sorpresa 

¡Bienvenida/o a tu backend más delicioso! Esta API te permite registrar usuarios, agregar desayunos con inventario dinámico, gestionar pedidos y más... todo con lógica automática para saber si hay ingredientes disponibles. 
¡Porque nadie quiere un desayuno que no se pueda servir!



## 🚀 ¿Qué puedes hacer con esta API?

- **Registrar usuarios** (`cliente` o `admin`) 👩‍🍳  
- **Login** con token JWT 🍪  
- **Agregar dirección** para tus pedidos 📍  
- **Crear inventario** con cantidad disponible 🥖  
- **Diseñar desayunos** y asociar ingredientes 🍳  
- **Verificar disponibilidad automática** ✅  
- **Hacer pedidos** como cliente (si hay stock) 🛍️  



## 🧱 Tecnologías

- Django 5.2  
- Django REST Framework  
- MySQL  
- JWT (djangorestframework-simplejwt)  
- Señales (`signals.py`) para manejar la lógica deliciosa ✨  



## 🧪 Cómo probar la API

1. **Levanta el servidor:**
    ```sh
    python manage.py runserver
    ```
2.Crea un usuario cliente: POST a /api/registrar-cliente/
3.Haz login y guarda tu token JWT: POST a /api/login/
4.Usa el token en el header:
 ```sh
Authorization: Bearer <tu_token>
  ```
5.Crea dirección, desayunos, inventario y... ¡haz un pedido!



## 💡 Lógica Automágica

✅ Si creas o modificas el inventario o ingredientes → la disponibilidad del desayuno se actualiza solita gracias a las señales.
❌ Si un ingrediente necesario está en cero → el desayuno se marca automáticamente como no disponible.


## 🔐 Roles y permisos

1.Admin: Puede crear desayunos, inventario, ingredientes.
2.Cliente: Solo puede hacer pedidos y ver información.

## 🥚 ¿Y si algo falla?
Revisa:

1.Que el token esté actualizado (no expirado).
2.Que el desayuno tenga inventario suficiente.
3.Que el usuario tenga tipo "cliente" para hacer pedidos.

## 🌮 Autora
Creado con mucho   amor por una desarrolladora  💻💜

![image](https://github.com/user-attachments/assets/52a20c33-c7d0-4599-aaf2-462c415e8c24)


