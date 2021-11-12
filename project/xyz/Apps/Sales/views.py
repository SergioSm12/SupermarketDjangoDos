from django.shortcuts import render, redirect, get_object_or_404,get_list_or_404
from .models import *
from django.views.generic import ListView
from .forms import *

# Create your views here.
def home(request):
    data ={
        'products' : Product.objects.all(),
    }

    return render(request, 'Home.html', data)


def createProduct(request):
    data = {
        'form': ProductForm()
    }
    if request.method == 'POST':
        formulario = ProductForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Guardado Correctamente"
        else:
            data["form"] = formulario
    return render(request, 'product/createProduct.html', data)

def editProduct(request, id_product):
    products= get_object_or_404(Product, id_product=id_product)
    data = {
        'form': ProductForm(instance=products)
    }

    if request.method == 'POST':
        formulario=ProductForm(data=request.POST, instance= products,)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='/')
        data['form'] = formulario
    return  render(request,'product/editProduct.html', data )

def deleteProduct(request,id_product):
    product=Product.objects.get(id_product=id_product)
    product.delete()
    return  redirect('/')

def listTypeProduct(request):
    productTypeList=ProductType.objects.all()
    return render(request, 'TypeProduct/listTypeProduct.html', {'productTypeList': productTypeList})

def createProductType(request):
    data = {
        'form': ProductTypeForm()
    }
    if request.method == 'POST':
        formulario = ProductTypeForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='listTypeProduct')
        else:
            data["form"] = formulario
    return render(request, 'TypeProduct/createProductType.html', data )

def editProductType(request, id_product_type):
    products_type= get_object_or_404(ProductType, id_product_type=id_product_type)
    data = {
        'form': ProductTypeForm(instance=products_type)
    }

    if request.method == 'POST':
        formulario=ProductTypeForm(data=request.POST, instance= products_type)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='listTypeProduct')
        data['form'] = formulario
    return render(request,'TypeProduct/editProductType.html', data )

def deleteProductType(request,id_product_type):
    productType=ProductType.objects.get(id_product_type=id_product_type)
    productType.delete()
    return redirect(to='listTypeProduct')

def listProvider(request):
    provider=ProductProvider.objects.all()
    return render(request, 'Provider/listProvider.html', {'provider': provider})

def  providerData(request,id_provider):
    providers = get_object_or_404(Provider, id_provider=id_provider)
    data = {
        'form': ProviderForm(instance=providers)
    }

    if request.method == 'POST':
        formulario = ProviderForm(data=request.POST, instance=providers, )
        if formulario.is_valid():
            formulario.save()
            return redirect(to='listProvider')
        data['form'] = formulario
    return render(request, 'Provider/providerData.html', data)

def list2Provider(request):
    provider=Provider.objects.all()
    return render(request, 'Provider/gestionProvider.html', {'provider': provider})

def createProvider(request):
    data = {
        'form': ProviderForm()
    }
    if request.method == 'POST':
        formulario = ProviderForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='list2Provider')
        else:
            data["form"] = formulario
    return render(request, 'Provider/createProvider.html', data)

def deleteProvider(request,id_provider):
    provider = Provider.objects.get(id_provider=id_provider)
    provider.delete()
    return redirect(to='list2Provider')


def createProductProvider(request):
    data = {
        'form': ProductProviderForm()
    }
    if request.method == 'POST':
        formulario = ProductProviderForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='listProvider')
        else:
            data["form"] = formulario
    return render(request, 'Provider/createProductProvider.html', data)