from django.db import models

class Procedimento(models.Model):
    procedimento = models.TextField()
    
    def __str__(self):
        return self.procedimento