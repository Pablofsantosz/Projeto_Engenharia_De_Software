"""
URL configuration for Projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views  # importa tudo da pasta views

urlpatterns = [
    path('homepage/', views.aplicacao_homepage, name = 'homepage'),
    path('perfil/', views.aplicacao_perfil, name = 'perfil'),
    path('excluir/', views.aplicacao_excluir, name = 'excluir'),
    path('editar/', views.aplicacao_editar, name='editar'),
    
    
     # URLs for new features
     #
    
    path('gerar-receita/', views.gerar_receita, name='gerar_receita'),
    path('receitas/', views.acessar_receitas, name='acessar_receitas'),
    path('receitas/<int:template_id>/', views.detalhe_receita, name='detalhe_receita'),
    path('receitas/<int:template_id>/imprimir/', views.imprimir_receita, name='imprimir_receita'),
    path('historico/', views.historico_atendimento, name='historico_atendimento'),
    path('historico/consulta/<int:consulta_id>/ver-receita/', views.ver_receita_salva, name='ver_receita_salva'),

]
