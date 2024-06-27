from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('index', index, name='index'),
    path('clients', clients, name='clients'),
    path('products', products, name='products'),
    path('shipments', shipments, name='shipments'),
]