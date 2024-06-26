from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    return render(request, 'entities/index.html')

def about(request):
    return render(request, 'entities/about.html')

def clients(request):
    context = {'clients': Client.objects.all()}
    return render(request, 'entities/clients.html', context)

def contact(request):
    return render(request, 'entities/contact.html')

def services(request):
    return render(request, 'entities/services.html')

def team(request):
    return render(request, 'entities/team.html')