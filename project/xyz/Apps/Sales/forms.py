from django import forms
from .models import Product, ProductType, Provider, ProductProvider

class ProductForm(forms.ModelForm):
    class Meta:
        model= Product
        fields= '__all__'

class ProductTypeForm(forms.ModelForm):
    class Meta:
        model= ProductType
        fields= '__all__'


class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = '__all__'

class ProductProviderForm(forms.ModelForm):
    class Meta:
        model = ProductProvider
        fields = '__all__'