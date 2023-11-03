from django.db import models

# Create your models here.
class variables(models.Model):
    temperatura = models.FloatField(max_length=4)
    humedad = models.FloatField(max_length=4)
    fecha = models.DateTimeField()
    def __str__(self):
        texto = "T°C:{0} H%:{1} Fecha:{2}"
        return texto.format(self.temperatura, self.humedad, self.fecha)