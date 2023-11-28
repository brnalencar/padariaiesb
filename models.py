from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=255)

class Pedido(models.Model):
    cliente = models.CharField(max_length=100)
    produtos = models.ManyToManyField(Produto)