from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum
from .models import Car, CarInventory


@receiver(post_save, sender=Car)
def update_create_inventory(sender, instance, **kwargs):
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        total_value = Sum('value')
    )['total_value']
    CarInventory.objects.create(
        cars_count=cars_count,
        cars_value=cars_value
    )

@receiver(post_delete, sender=Car)
def update_delete_inventory(sender, instance, **kwargs):
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        total_value = Sum('value')
    )['total_value']
    CarInventory.objects.create(
        cars_count=cars_count,
        cars_value=cars_value
    )