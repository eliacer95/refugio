from django.db import models

# Create your models here.
class Persona(models.Model):
	nombre = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=70)
	edad = models.IntegerField(default=0)
	telefono = models.CharField(max_length=12)
	email_field = models.EmailField()
	domicilio = models.TextField()

	def __str__(self):
		return '{}'.format(self.nombre, self.apellidos)

class Solicitud(models.Model):
	persona = models.ForeignKey(Persona, null=True, blank=True)
	numero_mascotas = models.IntegerField()
	razones = models.TextField()