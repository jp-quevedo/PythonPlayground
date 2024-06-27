from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    return render(request, 'entities/index.html')

def index(request):
    return render(request, 'entities/index.html')

def clients(request):
    context = {'clients': Client.objects.all()}
    return render(request, 'entities/clients.html', context)

def products(request):
    return render(request, 'entities/products.html')

def shipments(request):
    return render(request, 'entities/shipments.html')