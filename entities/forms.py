from django import forms

class ClientForm(forms.Form):
    name = forms.CharField(max_length=15, required=True)
    segment = forms.CharField(max_length=15, required=True)
    email = forms.EmailField(required=True)

class ProductForm(forms.Form):
    title = forms.CharField(max_length=15, required=True)
    category = forms.CharField(max_length=15, required=True)
    fragile = forms.BooleanField(required=False)