from django.db import models

# Create your models here.

class Shipment(models.Model):
    shipment_id = models.IntegerField()
    shipment_mode = models.CharField(max_length=15)
    price = models.IntegerField()
    date = models.DateField()
    completed = models.BooleanField()

class Client(models.Model):
    client_id = models.IntegerField()
    name = models.CharField(max_length=15)
    segment = models.CharField(max_length=15)
    email = models.EmailField()

class Product(models.Model):
    product_id = models.IntegerField()
    name = models.CharField(max_length=15)
    category = models.CharField(max_length=15)
    fragile = models.BooleanField()