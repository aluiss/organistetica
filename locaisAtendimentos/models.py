from django.db import models

class LocaisAtendimento(models.Model):
    local = models.TextField()
    endereco = models.TextField(max_length=250)

    def __str__(self):
        return self.local