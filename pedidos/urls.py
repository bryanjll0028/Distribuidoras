from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "pedidos"

urlpatterns = [
    path("tienda/", views.Procesar_pedido, name="procesar_pedido"),
]
