from django.db import models
from django.contrib.auth import get_user_model
from portfolio.models import Producto
from django.db.models import F, Sum, FloatField

User = get_user_model()


class Pedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(
            self.id
        )  # Convertimos el ID a cadena para que sea compatible con __str__

    @property
    def total(self):
        return (
            self.lineapedido_set.aggregate(
                total=Sum(F("pecio") * ("cantidad"), output_field=FloatField)
            )["total"]
            or 0
        )

    class Meta:
        db_table = "pedidos"
        verbose_name = "pedido"
        verbose_name_plural = "pedidos"
        ordering = ["id"]


class LineaPedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # Corregido el nombre del campo

    def __str__(self):
        return f"{self.cantidad} Unidades de {self.producto.nombre}"

    class Meta:
        db_table = "lineapedido"
        verbose_name = "Linea Pedido"
        verbose_name_plural = "Lineas Pedidos"
        ordering = ["id"]
