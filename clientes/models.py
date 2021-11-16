from django.db import models

class Clientes(models.Model):
    estado_civil_escolha = [
        ('st', 'Solteira(o'),
        ('cs', 'Casada(o)'),
        ('dv', 'Divorciada(o)')
    ]
    sexo_escolha = [
        ('fm', 'Feminino'),
        ('ms', 'Masculino'),
    ]
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField()
    foto = models.ImageField(upload_to='fotos/', blank=True)
    obs = models.TextField(max_length=400)
    endereco = models.CharField(max_length=300)
    cep = models.TextField(max_length=9)
    sexo = models.TextField(max_length=2, choices=sexo_escolha, default='fm')
    estado_civil = models.TextField(max_length=2, choices=estado_civil_escolha, default='st')
    email = models.EmailField()
    rg = models.TextField(max_length=12)
    cpf = models.TextField(max_length=14)

    def __str__(self):
        return self.nome

class Anamnese(models.Model):
    altura = models.FloatField(max_length=4)
    peso = models.FloatField(max_length=6)