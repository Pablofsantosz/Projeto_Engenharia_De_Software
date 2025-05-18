from django.http import HttpResponse  # usado para enviar texto de resposta

# função exibir na tela do teste_view
def teste_view(request):
    return HttpResponse('Essa é a rota de teste!')

def index_view(request):
    return HttpResponse('<h1>BEM VINDO!!</h1>')