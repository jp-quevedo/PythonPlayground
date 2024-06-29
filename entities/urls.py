from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('index', index, name='index'),
    path('clients', clients, name='clients'),
    path('products', products, name='products'),
    path('shipments', shipments, name='shipments'),

    path('client_form', clientForm, name='clientForm'),
    path('product_form', productForm, name='productForm'),

    path('client_filter', clientFilter, name='clientFilter'),
    path('client_filter_resp', clientFilterResp, name='clientFilterResp'),
]