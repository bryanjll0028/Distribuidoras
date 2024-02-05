from django.contrib import admin
from django.urls import path, include
from .views import Vregistro

app_name = "authentication"

urlpatterns = [
    path("", Vregistro.as_view(), name="registro"),
]
