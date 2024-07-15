from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from .models import *
from .forms import *

# Home

def home(request):
    return render(request, 'entities/index.html')

def index(request):
    return render(request, 'entities/index.html')

# Clients

def clients(request):
    context = {'clients': Client.objects.all()}
    return render(request, 'entities/clients.html', context)

def clientForm(request):
    if request.method == "POST":
        myForm = ClientForm(request.POST)
        if myForm.is_valid():
            client_name = myForm.cleaned_data.get("name")
            client_segment = myForm.cleaned_data.get("segment")
            client_email = myForm.cleaned_data.get("email")
            client = Client(name=client_name, segment=client_segment, email=client_email)
            client.save()
            context = {"clients": Client.objects.all()}
            return render(request, 'entities/clients.html', context)
    else:
        myForm = ClientForm()
    return render(request, "entities/clientForm.html", {"form": myForm})

def clientFilter(request):
    return render(request, "entities/clientFilter.html")

def clientFilterResp(request):
    if request.GET["filter"]:
        filter = request.GET["filter"]
        clients = Client.objects.filter(name__icontains=filter)
        context = {'clients': clients}
    else:
        context = {'clients': Client.objects.all()}
    return render(request, 'entities/clients.html', context)

def clientUpdate(request, client_id):
    client = Client.objects.get(id = client_id)
    if request.method == "POST":
        myForm = ClientForm(request.POST)
        if myForm.is_valid():
            client.name = myForm.cleaned_data.get("name")
            client.segment = myForm.cleaned_data.get("segment")
            client.email = myForm.cleaned_data.get("email")
            client.save()
            context = {"clients": Client.objects.all()}
            return render(request, 'entities/clients.html', context)
    else:
        myForm = ClientForm(initial = {"name": client.name, "segment": client.segment, "email": client.email})
    return render(request, "entities/clientForm.html", {"form": myForm})

def clientDelete(request, client_id):
    client = Client.objects.get(id = client_id)
    client.delete()
    context = {"clients": Client.objects.all()}
    return render(request, 'entities/clients.html', context)

# Products

def products(request):
    context = {'products': Product.objects.all()}
    return render(request, 'entities/products.html', context)

def productForm(request):
    if request.method == "POST":
        myForm = ProductForm(request.POST)
        if myForm.is_valid():
            product_title = myForm.cleaned_data.get("title")
            product_category = myForm.cleaned_data.get("category")
            product_fragile = myForm.cleaned_data.get("fragile")
            product = Product(title=product_title, category=product_category, fragile=product_fragile)
            product.save()
            context = {"products": Product.objects.all()}
            return render(request, 'entities/products.html', context)
    else:
        myForm = ProductForm()
    return render(request, "entities/productForm.html", {"form": myForm})

def productUpdate(request, product_id):
    product = Product.objects.get(id = product_id)
    if request.method == "POST":
        myForm = ProductForm(request.POST)
        if myForm.is_valid():
            product.title = myForm.cleaned_data.get("title")
            product.category = myForm.cleaned_data.get("category")
            product.fragile = myForm.cleaned_data.get("fragile")
            product.save()
            context = {"products": Product.objects.all()}
            return render(request, 'entities/products.html', context)
    else:
        myForm = ProductForm(initial = {"title": product.title, "category": product.category, "fragile": product.fragile})
    return render(request, "entities/productForm.html", {"form": myForm})

def productDelete(request, product_id):
    product = Product.objects.get(id = product_id)
    product.delete()
    context = {"products": Product.objects.all()}
    return render(request, 'entities/products.html', context)

# Shipments

# def shipments(request):
#     context = {'shipments': Shipment.objects.all()}
#     return render(request, 'entities/shipments.html', context)

class ShipmentList(ListView):
    model = Shipment

class CreateShipment(CreateView):
    model = Shipment
    fields = ["shipment_mode", "price", "date", "completed"]
    success_url = reverse_lazy("shipments")

class UpdateShipment(UpdateView):
    model = Shipment
    fields = ["shipment_mode", "price", "date", "completed"]
    success_url = reverse_lazy("shipments")

class DeleteShipment(DeleteView):
    model = Shipment
    success_url = reverse_lazy("shipments")