from django.shortcuts import render
from .models import Usuario
from .forms import UsuarioRegisterForm

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

def electrica(request):
    context = {}
    return render(request, "pages/electrica.html", context)

def mtb(request):
    context = {}
    return render(request, "pages/mtb.html", context)

def nino(request):
    context = {}
    return render(request, "pages/nino.html", context)

def ruta(request):
    context = {}
    return render(request, "pages/ruta.html", context)

def urbex(request):
    context = {}
    return render(request, "pages/urbex.html", context)

def mostrar_registro(request):
    context = {}
    return render(request, "pages/mostrar_registro.html", context)

def crear_usuario(request):
    context = {}
    return render(request, "pages/crear_usuario.html", context)

def crud(request):
    usuarios = Usuario.objects.all()
    context = {"usuarios": usuarios}
    return render(request, "pages/usuario_list.html", context)

def registro_vista(request):

    if request.method == "POST":
        form = UsuarioRegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
    else:
        print("usuario no registrado")

    form = UsuarioRegisterForm()
    context = {
        'form':  form
    }
    return render (request, "pages/sign-up.html", context)
    
def usuarios_del(request, pk):
    context = {}
    try:
        usuario = Usuario.objects.get(nombre=pk)

        usuario.delete()
        mensaje = "Bien, datos borrados"
        usuarios = Usuario.objects.all()
        context = {'usuarios': usuarios, 'mensaje': mensaje}
        return render(request, "pages/usuario_list.html", context)
    except:
        mensaje = "Error, rut no existe"
        usuarios = Usuario.objects.all()
        context = {'usuarios': usuarios, 'mensaje': mensaje}
        return render(request, "pages/usuario_list.html", context)
    
def usuarios_findEdit(request, pk):

    if pk != "":
        usuario = Usuario.objects.get(nombre=pk)

        context={'usuario': usuario}
        if usuario:
            return render(request, "pages/editar_registro.html", context)
        else:
            context = {'mensaje': "Error nombre no existe"}
            return render(request, "pages/usuario_list.html", context)
        
def usuariosUpdate(request):

    if request.method == "POST":
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        email = request.POST["email"]
        password = request.POST["password"]

        usuarios = Usuario()
        usuarios.nombre=nombre
        usuarios.apellido=apellido
        usuarios.email=email
        usuarios.password=password
        usuarios.save()

        context = {'mensaje': "Ok, datos actualizados", 'usuarios': usuarios}
        return render(request, "pages/editar_registro.html", context)
    else:
        usuarios = Usuario.objects.all()
        context = {'usuarios': usuarios}
        return render(request, "pages/usuario_list.html", context)
    
