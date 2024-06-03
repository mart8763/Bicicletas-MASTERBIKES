from django.shortcuts import render

# Create your views here.

def index(request):
    """context: paquete variables que pueden ser consumidas por el front"""
    context = {}
    return render(request, "pages/index.html", context)