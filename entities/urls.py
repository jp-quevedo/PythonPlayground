from django.urls import path

from .views import *

urlpatterns = [

    # Home

    path('', home, name='home'),
    path('index', index, name='index'),

    # Clients

    path('clients', clients, name='clients'),
    path('client_form', clientForm, name='clientForm'),
    path('client_filter', clientFilter, name='clientFilter'),
    path('client_filter_resp', clientFilterResp, name='clientFilterResp'),
    path('client_update/<client_id>/', clientUpdate, name='clientUpdate'),
    path('client_delete/<client_id>/', clientDelete, name='clientDelete'),

    # Products

    path('products', products, name='products'),
    path('product_form', productForm, name='productForm'),
    path('product_update/<product_id>/', productUpdate, name='productUpdate'),
    path('product_delete/<product_id>/', productDelete, name='productDelete'),

    #Shipments

    # path('shipments', shipments, name='shipments'),
    path('shipments', ShipmentList.as_view(), name='shipments'),
    path('shipment_create', CreateShipment.as_view(), name='createShipment'),
    path('shipment_update/<int:pk>/', UpdateShipment.as_view(), name='updateShipment'),
    path('shipment_delete/<int:pk>/', DeleteShipment.as_view(), name='deleteShipment'),

]