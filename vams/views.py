from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .models import Productos


# Create your views here.
def inicio(request):
    return render(request, 'index.html')


def servicios(request):
    return render(request, 'servicios.html')


def nosotros(request):
    return render(request, 'sobrenosotros.html')


def catalogo01(request):
    return render(request, 'aretes.html')


def catalogo02(request):
    return render(request, 'collares.html')

def collares_view(request):
    collares = Productos.objects.filter(categoria_producto='Collares')
    return render(request, 'collares.html', {'productos': collares})

def aretes_view(request):
    aretes = Productos.objects.filter(categoria_producto='Aretes')
    return render(request, 'aretes.html', {'productos': aretes})


@login_required
def cerrarsesion(request):
    logout(request)
    return redirect('index.html')


def ingresar(request):
    if request.method == 'GET':
        return render(request, 'InicioSesion.html', {'form': AuthenticationForm})
    else:
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password'],
        )
        if user is None:
            return render(
                request,
                'inicioSesion.html',
                {
                    'form': AuthenticationForm,
                    'error': 'Usuario o contraseña es incorrecto',
                },
            )
        else:
            login(request, user)
            return redirect('http://127.0.0.1:8000/admin/')
