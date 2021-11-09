from django.db import models

class Procedimento(models.Model):
    procedimento = models.TextField()
    valor = models.IntegerField()
    
    def __str__(self):
        return self.procedimento