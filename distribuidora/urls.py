"""
URL configuration for distribuidora project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from core import views as core_views
from portfolio.urls import portfolio_patterns
from django.conf import settings

urlpatterns = [
    path("", core_views.home, name="home"),
    path("home/", core_views.inicio, name="home"),
    path("servicio/", core_views.servicio, name="servicio"),
    path("registrarse/", core_views.registrarse, name="registrarse"),
    path("logout/", core_views.exit, name="exit"),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("portfolio/", include(portfolio_patterns)),
    path("carro/", include("carro.urls")),
    path("pedidos/", include("pedidos.urls")),
    path("autentication/", include("autentication.urls")),
]
if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
