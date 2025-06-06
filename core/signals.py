from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import IngredienteDesayuno, Inventario, Desayuno


def actualizar_disponibilidad_desayuno(desayuno):
    ingredientes = IngredienteDesayuno.objects.filter(desayuno=desayuno)
    for ingrediente in ingredientes:
        if ingrediente.item.cantidad_disponible < ingrediente.cantidad_necesaria:
            if desayuno.disponibilidad: 
                desayuno.disponibilidad = False
                Desayuno.objects.filter(id=desayuno.id).update(disponibilidad=False)
            return
    if not desayuno.disponibilidad:  
        Desayuno.objects.filter(id=desayuno.id).update(disponibilidad=True)


@receiver(post_save, sender=IngredienteDesayuno)
@receiver(post_delete, sender=IngredienteDesayuno)
def actualizar_por_ingrediente(sender, instance, **kwargs):
    actualizar_disponibilidad_desayuno(instance.desayuno)


@receiver(post_save, sender=Inventario)
@receiver(post_delete, sender=Inventario)
def actualizar_por_inventario(sender, instance, **kwargs):
    desayunos_afectados = Desayuno.objects.filter(
        ingredientes__item=instance
    ).distinct()
    for desayuno in desayunos_afectados:
        actualizar_disponibilidad_desayuno(desayuno)


@receiver(post_save, sender=Desayuno)
def actualizar_por_desayuno(sender, instance, **kwargs):
    actualizar_disponibilidad_desayuno(instance)
