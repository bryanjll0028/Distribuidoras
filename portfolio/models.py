from django.db import models


class Tipo(models.Model):
    nombre_tipo = models.CharField(max_length=50, default="valor_predeterminado")
    image = models.ImageField(verbose_name="imagen", upload_to="projects")

    class Meta:
        verbose_name = "Tipo"
        verbose_name_plural = "Tipos"
        ordering = ["nombre_tipo"]

    def __str__(self):
        return self.nombre_tipo


class Marca(models.Model):
    nombre = models.CharField(max_length=200)
    nombre_proveedor = models.CharField(max_length=100, default="valor_predeterminado")

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
        ordering = ["-nombre"]

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "Categorías"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    producto_id = models.CharField(max_length=10, unique=True, default=1)
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    descripcion = models.TextField()
    nuevo = models.BooleanField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, default=1)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, default=1
    )  # Nueva relación con la tabla Categoria
    fecha_fabricacion = models.DateField()
    image = models.ImageField(verbose_name="imagen", upload_to="projects")
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "Articulos"
        ordering = ["-nombre"]

    def __str__(self):
        return self.nombre
