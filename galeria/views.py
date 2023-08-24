from django.shortcuts import render, get_object_or_404

# from django.http import HttpResponse
from galeria.models import Fotografia


def index(request):
    # return HttpResponse('<h1>Alura Space</h1><p>Bem vindo ao espaço</p>')

    #    fotografias = {
    #    1:{"nome":"Nebulosa de Carina",
    #       "legenda":"webtelescope.org/NASA/James Webb"},
    #    2:{"nome":"Galáxia NGC 1979",
    #       "legenda":"NASA.org/NASA/Hubble"},
    #    }
    # fotografias = Fotografia.objects.all()
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
    # fotografias = Fotografia.objects.filter(publicada=True)
    #    return render(request, 'galeria/index.html', {"cards":fotografias})
    return render(request, "galeria/index.html", {"cards": fotografias})


def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, "galeria/imagem.html", {"fotografia": fotografia})


def buscar(request):
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
    if "buscar" in request.GET:
        nome_a_buscar = request.GET["buscar"]
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render(request, "galeria/buscar.html", {"cards": fotografias})
