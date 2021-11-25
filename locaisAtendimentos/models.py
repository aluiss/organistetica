from django.db import models

class LocaisAtendimento(models.Model):
    local = models.TextField(max_length=100)
    endereco = models.TextField(max_length=150)

    def __str__(self):
        return self.local