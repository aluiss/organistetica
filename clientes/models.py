from django.db import models

class Clientes(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField()
    altura = models.FloatField(max_length=4)
    peso = models.FloatField(max_length=6)
    endereco = models.CharField(max_length=300)
    foto = models.ImageField(upload_to='fotos/', blank=True)
    obs = models.TextField(max_length=400)

    def __str__(self):
        return self.nome