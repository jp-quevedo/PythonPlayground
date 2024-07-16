from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from django.views.generic import UpdateView
from .models import *
from .forms import *

# Home

def home(request):
    return render(request, 'entities/index.html')

def index(request):
    return render(request, 'entities/index.html')

def about(request):
    return render(request, 'entities/about.html')

# Clients

@login_required
def clients(request):
    context = {'clients': Client.objects.all()}
    return render(request, 'entities/clients.html', context)

@login_required
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

@login_required
def clientFilter(request):
    return render(request, "entities/clientFilter.html")

@login_required
def clientFilterResp(request):
    if request.GET["filter"]:
        filter = request.GET["filter"]
        clients = Client.objects.filter(name__icontains=filter)
        context = {'clients': clients}
    else:
        context = {'clients': Client.objects.all()}
    return render(request, 'entities/clients.html', context)

@login_required
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

@login_required
def clientDelete(request, client_id):
    client = Client.objects.get(id = client_id)
    client.delete()
    context = {"clients": Client.objects.all()}
    return render(request, 'entities/clients.html', context)

# Products

@login_required
def products(request):
    context = {'products': Product.objects.all()}
    return render(request, 'entities/products.html', context)

@login_required
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

@login_required
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

@login_required
def productDelete(request, product_id):
    product = Product.objects.get(id = product_id)
    product.delete()
    context = {"products": Product.objects.all()}
    return render(request, 'entities/products.html', context)

# Shipments

# def shipments(request):
#     context = {'shipments': Shipment.objects.all()}
#     return render(request, 'entities/shipments.html', context)

class ShipmentList(LoginRequiredMixin, ListView):
    model = Shipment

class CreateShipment(LoginRequiredMixin, CreateView):
    model = Shipment
    fields = ["shipment_mode", "price", "date", "completed"]
    success_url = reverse_lazy("shipments")

class UpdateShipment(LoginRequiredMixin, UpdateView):
    model = Shipment
    fields = ["shipment_mode", "price", "date", "completed"]
    success_url = reverse_lazy("shipments")

class DeleteShipment(LoginRequiredMixin, DeleteView):
    model = Shipment
    success_url = reverse_lazy("shipments")

# Login - Logout - Signup

def loginRequest(request):
    if request.method == "POST":
        username_requested = request.POST["username"]
        password_requested = request.POST["password"]
        user = authenticate(request, username = username_requested, password = password_requested)
        if user is not None:
            login(request, user)
            try:
                avatar = Avatar.objects.get(user=request.user.id).image.url
            except:
                avatar = "/media/avatars/default.png"
            finally:
                request.session["avatar"] = avatar
            return render(request, "entities/index.html")
        else:
            return redirect(reverse_lazy('login'))
    else:
        myForm = AuthenticationForm()
    return render(request, "entities/login.html", {"form": myForm})

def signupRequest(request):
    if request.method == "POST":
        myForm = SignupForm(request.POST)
        if myForm.is_valid():
            user = myForm.cleaned_data.get("username")
            myForm.save()
            return redirect(reverse_lazy('home'))
    else:
        myForm = SignupForm()
    return render(request, "entities/signup.html", {"form": myForm})

# Profile editing

@login_required
def editProfile(request):
    user_requested = request.user
    if request.method == 'POST':
        myForm = EditUserForm(request.POST)
        if myForm.is_valid():
            user = User.objects.get(username=request.user)
            user.email = myForm.cleaned_data.get("email")
            user.first_name = myForm.cleaned_data.get("first_name")
            user.last_name = myForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy('home'))
        else:
            myForm = EditUserForm(instance=user_requested)
    return render(request, "entities/edit_profile.html", {"form": myForm})


class NewPassword(LoginRequiredMixin, PasswordChangeView):
    template_name = 'entities/new_password.html'
    success_url = reverse_lazy('home')

@login_required
def addAvatar(request):
    if request.method == 'POST':
        myForm = AvatarForm(request.POST, request.FILES)
        if myForm.is_valid():
            user_requested = User.objects.get(username=request.user)
            image_requested = myForm.cleaned_data["image"]
            old_avatar = Avatar.objects.filter(user=user_requested)
            if len(old_avatar) > 0:
                for i in range(len(old_avatar)):
                    old_avatar[i].delete()
            avatar = Avatar(user=user_requested, image=image_requested)
            avatar.save()
            image = Avatar.objects.get(user=user_requested).image.url
            request.session["avatar"] = image
            return redirect(reverse_lazy('home'))
    else:
        myForm = AvatarForm()
    return render(request, 'entities/add_avatar.html', {'form': myForm})