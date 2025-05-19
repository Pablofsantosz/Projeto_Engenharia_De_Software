# MODELAÇÃO DO BANCO DE DADOS

from django.db import models

# Create your models here.
class Usuario(models.Model):    # Criando objeto tarefa
    nome = models.CharField(max_length=100)     # CharField com no máximo 100 caracteres
    cpf = models.CharField(max_length=14, unique=True)     
    crm = models.CharField(max_length=20)     # BooleanField de completo inicializado como falso
    email = models.EmailField(unique=True)    # auto_now_add registra automaticamente a data ao ser criado
    senha = models.CharField(max_length=100)    # Pode usar hashing depois

    def __str__(self):  # Faz o nome das tarefas aparecerem na hora do print
        return self.nome