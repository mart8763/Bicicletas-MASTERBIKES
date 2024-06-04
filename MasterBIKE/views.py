from django.shortcuts import render

# Create your views here.

def index(request):
    """context: paquete variables que pueden ser consumidas por el front"""
    context = {}
    return render(request, "pages/index.html", context)

def productos(request):
    context = {}
    return render(request, "pages/productos.html", context)

def categoria(request):
    context = {}
    return render(request, "pages/categoria.html", context)

def carro(request):
    context = {}
    return render(request, "pages/carro.html", context)

def registro(request):
    context = {}
    return render(request, "pages/registro.html", context)

def iniciar_sesion(request):
    context = {}
    return render(request, "pages/iniciar_sesion.html", context)

def termino_y_condiciones(request):
    context = {}
    return render(request, "pages/termino_y_condiciones.html", context)