# MODELAÇÃO DO BANCO DE DADOS

from django.db import models

# Create your models here.
class Usuario(models.Model):    # Criando objeto Usuario
    nome = models.CharField(max_length=100)    
    cpf = models.CharField(max_length=14, unique=True)     
    crm = models.CharField(max_length=20)     
    email = models.EmailField(unique=True)    
    senha = models.CharField(max_length=100)    

    def __str__(self):  # Faz o nome das tarefas aparecerem na hora do print
        return self.nome