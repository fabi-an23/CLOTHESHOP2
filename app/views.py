from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ContactoForms


# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def contacto(request):
    data = {
        'form': ContactoForms()
    }

    if request.method =='POST':
        formulario = ContactoForms(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto Guardado"
        else:
            data["form"] = formulario

    return render(request, 'app/contacto.html', data)

def hombre(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/hombre.html', data)

def login(request):
    return render(request, 'app/login.html')

def mujer(request):
    return render(request, 'app/mujer.html')

def registro(request):
    return render(request, 'app/registro.html')

def carrito(request):
    
    return render(request, 'app/carrito.html')

