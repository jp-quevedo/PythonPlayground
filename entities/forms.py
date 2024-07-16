from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ClientForm(forms.Form):
    name = forms.CharField(max_length=15, required=True)
    segment = forms.CharField(max_length=15, required=True)
    email = forms.EmailField(required=True)

class ProductForm(forms.Form):
    title = forms.CharField(max_length=15, required=True)
    category = forms.CharField(max_length=15, required=True)
    fragile = forms.BooleanField(required=False)

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class EditUserForm(UserChangeForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label="First Name", max_length=20, required=True)
    last_name = forms.CharField(label="Last Name", max_length=20, required=True)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]

class AvatarForm(forms.Form):
    image = forms.ImageField(required=True)