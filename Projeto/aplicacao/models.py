from django.db import models
from django.contrib.auth.models import User # Import Django's built-in User model

class CID(models.Model):
    """Represents a CID-10 code and its description."""
    codigo = models.CharField(max_length=10, unique=True, help_text="Ex: J06.9")
    descricao = models.CharField(max_length=255, help_text="Ex: Infecção aguda das vias aéreas superiores")

    def __str__(self):
        return f"{self.codigo} - {self.descricao}"

class ReceitaTemplate(models.Model):
    """A prescription template linked to a specific CID."""
    cid = models.ForeignKey(CID, on_delete=models.CASCADE, related_name="templates")
    titulo = models.CharField(max_length=200, help_text="Ex: Tratamento para Virose Comum")
    medicamentos = models.TextField(help_text="Liste os medicamentos e suas dosagens. Ex: Dipirona 500mg - 1 comp a cada 6h por 3 dias.")
    orientacoes_gerais = models.TextField(help_text="Ex: Manter repouso, beber bastante líquido.")

    def __str__(self):
        return self.titulo

   
class Consulta(models.Model):
    """Records a specific consultation with a patient."""
    medico = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="consultas")
    paciente_nome = models.CharField(max_length=100)
    paciente_cpf = models.CharField(max_length=14)
    # --- NOVOS CAMPOS ---
    paciente_idade = models.CharField(max_length=50, blank=True, null=True)
    paciente_peso = models.CharField(max_length=50, blank=True, null=True)
    # --------------------
    sintomas = models.TextField()
    cid_aplicado = models.ForeignKey(CID, on_delete=models.SET_NULL, null=True)
    data_consulta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Consulta de {self.paciente_nome} em {self.data_consulta.strftime('%d/%m/%Y')}"
    


class ReceitaPersonalizada(models.Model):
    """Guarda uma versão de uma receita que foi customizada por um médico."""
    medico = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receitas_personalizadas")
    cid = models.ForeignKey(CID, on_delete=models.CASCADE)
    titulo_personalizado = models.CharField(max_length=200)
    medicamentos_personalizados = models.TextField()
    orientacoes_personalizadas = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.titulo_personalizado} (Dr. {self.medico.username})'