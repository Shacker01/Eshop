from django.db import models
from django.contrib.auth.models import User


class Clients(models.Model):
    client = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=14, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Clients'

    def __str__(self):
        return f'{self.client}'

class Shop(models.Model):
    owner = models.OneToOneField(Clients, on_delete=models.CASCADE)
    category = models.CharField(max_length=30, blank=False)
    location = models.CharField(max_length=30, blank=False)
    
    def __str__(self):
        return f'{self.owner}'

class Items(models.Model):
    item = models.ForeignKey(Shop, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.item}'
    
    class Meta:
        verbose_name_plural = 'Items'