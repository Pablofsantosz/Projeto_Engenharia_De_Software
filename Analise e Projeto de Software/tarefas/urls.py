from django.urls import path
from . import views

app_name = 'tarefas'

urlpatterns = [
    path('', views.tarefas_home, name = 'home'),    
    # tarefas_adicionar agora trata de GET e POST
    path('adicionar/', views.tarefas_adicionar, name = 'adicionar'), # name para dar um nome á pagina
]
