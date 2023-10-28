from django.db import models

# Create your models here.
from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(null=True)

    def __str__(self):
        return self.nome
