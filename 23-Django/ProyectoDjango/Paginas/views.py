from django.shortcuts import render
from .models import Pagina

# Create your views here.


def pagina(request, dato):

    pagina = Pagina.objects.get(slug = dato)

    return render(request, 'paginas/pagina.html', {
        'page': pagina
    })
