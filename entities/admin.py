from django.contrib import admin

from .models import *

class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "segment", "email")

# Register your models here.

admin.site.register(Client, ClientAdmin)
admin.site.register(Product)
admin.site.register(Shipment)