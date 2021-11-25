from django.db import models

class Procedimento(models.Model):
    procedimento = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.procedimento