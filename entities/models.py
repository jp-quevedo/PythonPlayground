from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=15)
    segment = models.CharField(max_length=15)
    email = models.EmailField()

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    title = models.CharField(max_length=15)
    category = models.CharField(max_length=15)
    fragile = models.BooleanField()

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return f"{self.title}"
    
class Shipment(models.Model):
    shipment_mode = models.CharField(max_length=15, default='standard')
    price = models.IntegerField()
    date = models.DateField()
    completed = models.BooleanField()

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return f"{self.date}"