from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.

def home(request):
    return render(request, 'entities/index.html')

def index(request):
    return render(request, 'entities/index.html')

def clients(request):
    context = {'clients': Client.objects.all()}
    return render(request, 'entities/clients.html', context)

def products(request):
    context = {'products': Product.objects.all()}
    return render(request, 'entities/products.html', context)

def shipments(request):
    context = {'shipments': Shipment.objects.all()}
    return render(request, 'entities/shipments.html', context)

# Create your forms here.

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

# Create your filters here.

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