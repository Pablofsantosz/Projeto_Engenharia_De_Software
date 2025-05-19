from django.urls import path
from . import views

app_name = 'credenciamento'

urlpatterns = [
     
    # tarefas_adicionar agora trata de GET e POST
    path('cadastro/', views.credenciamento_cadastro, name = 'cadastro'), # name para dar um nome á pagina
]
