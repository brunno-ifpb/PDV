from django.db import models

# Create your models here.

class Produtos(models.Model):
    id_produto = models.AutoField(primary_key=True)

    nome = models.TextField(max_length=255)
    quantidade = models.IntegerField()
    valor = models.IntegerField()
    validade = models.TextField()
    lucro = models.IntegerField()
    img = models.ImageField()

