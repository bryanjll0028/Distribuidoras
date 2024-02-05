from django.urls import path
from . import views
from .views import ProductoListView, ProductoDetailView, TipoListView
from django.conf import settings


portfolio_patterns = (
    [
        path("", TipoListView.as_view(), name="tipo"),
        path("tienda/", views.tienda, name="Tienda"),
        path("producto/", ProductoListView.as_view(), name="producto"),
        path(
            "productos/tipo/<str:tipo>/",
            ProductoListView.as_view(),
            name="productos_por_tipo",
        ),
    ],
    "portfolio",
)
