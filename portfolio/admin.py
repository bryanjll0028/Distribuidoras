from django.contrib import admin
from .models import Marca, Tipo, Producto, Categoria


# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ("create", "update")


admin.site.register(Marca)
admin.site.register(Tipo)
admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)
