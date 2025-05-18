"""
URL configuration for projetoAPS project.

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

''' 
ROTAS DO SEU PROJETO (pontos de acesso)
 - LINKS POR EXEMPLO
'''

from django.contrib import admin
from django.urls import path, include
from . import views  # importa tudo da pasta views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teste/', views.teste_view), # precisa usar .views para referenciar
    path('', views.index_view),
    path('tarefas/', include('tarefas.urls')),
    # Com o inlcude, tudo dentro do 'urls' da pasta 'tarefas' vai ser acessado com '/tarefas/novoPath/'
    path('homepage/', include('homepage.urls')),
]