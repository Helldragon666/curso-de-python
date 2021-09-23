

from .models import Pagina

def get_Paginas(request):
    paginas = Pagina.objects.filter(visible=True).values_list('id', 'titulo', 'slug') # muestra un query_set con los valores seleccionados
    #argumento flat=True para mostrar un texto plano

    return {
        'paginas': paginas
    }