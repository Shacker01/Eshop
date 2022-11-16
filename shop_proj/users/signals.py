from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import *

@receiver(post_save, sender=User)
def create_client_account(sender, instance, created, **kwargs):
    if created:
        Clients.objects.create(client=instance)

@receiver(post_save, sender=Clients)
def create_client_account(sender, instance, created, **kwargs):
    if created:
        Shop.objects.create(owner=instance)

@receiver(post_save, sender=Items)
def create_client_account(sender, instance, created, **kwargs):
    if created:
        Items.objects.create(item=instance)
