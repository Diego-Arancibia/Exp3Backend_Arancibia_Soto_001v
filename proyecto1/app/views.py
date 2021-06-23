from django.db import reset_queries
from django.http import request
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ContactoForm, ProductoForm
from django.contrib import messages

# Create your views here.

def home (request):
    return render(request, 'app/home.html')

def contacto (request):
    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)   
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["form"] = formulario
    return render(request, 'app/contacto.html', data)


def galeria (request):
    return render(request, 'app/galeria.html')


def conocenos (request):
    return render(request, 'app/conocenos.html')

def intranet (request):
    return render (request, 'app/intranet.html')

def producto (request):
    productos = Producto.objects.all()
    data ={
        'productos' : productos
    }
    return render (request, 'app/productos.html', data)

def agregar_producto(request):
    data ={
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Producto Agregado")
            data["mensaje"]= "guardado correctamente"
        else:
            data["form"]     = formulario
    return render (request,'app/producto/agregar.html', data)

def listar_producto (request):
    productos = Producto.objects.all()
    data = {
        'productos' : productos
    }
    return render(request, 'app/producto/listar.html', data)

def modificar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)
    data={
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect (to=listar_producto)
        data["form"] = formulario
    return render (request, 'app/producto/modificar.html', data)

def eliminar_producto(request, id):
    producto= get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="listar_producto")

def apiferiados (request):
    return render (request, 'app/apiferiados.html')
