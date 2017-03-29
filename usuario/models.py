from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# Modelo de perfil de usuario que extiende al usuario Django
class Usuario(models.Model):
    # Referencia al usuario de Django
    user = models.ForeignKey(User)
    # Atributos extra
    nombres = models.CharField(max_length=50, null=False)
    apellidos = models.CharField(max_length=50, null=False)
    pais = models.CharField(max_length=50, null=True)
    ciudad = models.CharField(max_length=50, null=True)
    intereses = models.CharField(max_length=200, null=False)
    rol = models.CharField(max_length=200, null=False)

    def __str__(self):
        return '{}'.format(self.nombres)
