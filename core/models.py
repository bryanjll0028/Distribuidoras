from django.db import models


class marca(models.Model):
    nombre = models.CharField(max_length=30)
    procedencia = models.CharField(max_length=30)
