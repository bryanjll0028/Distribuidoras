from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout

# Create your views here.
html_base = """
     <h1>LA DISTRIBUIDORA</h1>
<ul>
        <li><a href="/home/">Portada</a></li>
        <li><a href="/servico/">Servico</a></li>
        <li><a href="/Somos/">Somos</a></li>
        <li><a href="/contacto/">Contactenos</a></li>
        <li><a href="/registrarse/">Registrarse</a></li>
        <li><a href="/portfolio/producto/">Productos</a></li>
       
</ul>
    """


def registrarse(request):
    return render(request, "core/registration/registrarse.html")


def home(request):
    return render(request, "core/home.html")


def inicio(request):
    return render(request, "core/home.html")


def servicio(request):
    return render(request, "core/servicio.html")


@login_required
def somos(request):
    return render(request, "core/somos.html")


def exit(request):
    logout(request)
    return redirect("home")
