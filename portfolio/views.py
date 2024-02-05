from django.shortcuts import render, get_object_or_404
from .models import Producto, Tipo
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


# Create your views here.
def tienda(request):
    productos = Producto.objects.all()
    return render(request, "portfolio/producto_list.html", {"productos": productos})


class ProductoListView(ListView):
    model = Producto

    def get_queryset(self):
        tipo = self.kwargs.get("tipo")
        if tipo:
            return Producto.objects.filter(tipo__nombre_tipo=tipo)
        else:
            return Producto.objects.all()


class ProductoDetailView(DetailView):
    model = Producto


class TipoListView(ListView):
    model = Tipo
