



import json


from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.core import serializers
from django.db.models import Q
from django.contrib import messages


from primeraApp.models import Articulo
from primeraApp.forms import FormArticulo


# Create your views here.

#from primeraApp.layouts import header
from datetime import datetime
fechaCompleta = datetime.now()


def index(request):

    # html =  '''
    #        <h1>Inicio</h1>
    #        <ul>
    #        '''
    #year = 2021

    # while year >= 2010:
    #    html += f'<li>{year}</li>'
    #    year -= 1

    #html += '</ul>'

    # return HttpResponse(header.layout + html)

    nombre = 'Yonatan'

    lenguajes = ['JavaScript', 'Python', 'PHP', 'C++']
    #lenguajes = []

    listayears = range((fechaCompleta.year - 11), (fechaCompleta.year + 1))

    return render(request, 'index.html', {
        'mi_variable': 'Soy un dato que está en la vista',
        'title': 'Inicio',
        'nombre': nombre,
        'lenguajes': lenguajes,
        'years': listayears.__reversed__(),
        'fecha': fechaCompleta.year
    })


def hola_mundo(request):

    #nombre = 'Yonatan'

    # return HttpResponse(header.layout + f'''
    #        <h1>Holi desde Django ;3</h1>
    #        <h3>Soy {nombre} :3</h3>
    # ''')

    return render(request, 'hola_mundo.html')


def pagina(request, redirigir=0):

    # if redirigir == 1:
    #    #return redirect('/')
    #    #return redirect('/contacto/yon/cerv')
    #    return redirect('contacto', nombre='Yonatan', apellido='Cervantes') # nombre de la url y parametros

    # html =  '''
    #        <h1>Página de mi web</h1>
    #        <p>Todos los derechos reservados</p>
    #        '''

    # return HttpResponse(header.layout + html)

    #return render(request, 'pagina.html', {'fecha': fechaCompleta.year})
    return render(request, 'pagina.html', {
        'texto': '',
        'lista': ['uno', 'dos', 'tres']
    })


def contacto(request, nombre='', apellido=''):  # parametro nombre y apelldo
    #html = ''

    # if nombre and apellido:
    #   html = f'<h3>{nombre} {apellido}</h3>'
    #

    # return HttpResponse(header.layout + f'<h2>Contacto</h2>' + html)

    #return render(request, 'contacto.html', context={'fecha': fechaCompleta.year})
    return render(request, 'contacto.html')


def crear_articulo(request, titulo, contenido, publico):

    articulo = Articulo(
        titulo= titulo,
        contenido= contenido,
        publico= publico
    )
    
    articulo.save()

    # Para retornar varios objetos JSON desde un modelo de BD

    #data = serializers.serialize('json', Articulo.objects.all()) # serializar en el objeto json
    #data = json.loads(data) # deserializar en una cadena json
    #return JsonResponse(data, safe=False) # Para serializar objetos que no sean dict, debe establecer el parámetro safe en False


    return HttpResponse(f'Artículo creado {articulo.titulo} - {articulo.contenido}')

    # Para retornar un objeto JSON

    #return JsonResponse({
    #    'msg': 'Artículo creado'
    #})

    # return JsonResponse({
    #     'msg': 'usuario creado',
    #     'usuario': {
    #         'id': 1,
    #         'name': 'Yonatan'
    #     }
    # })


def articulo(request):

    try:
        articulo = Articulo.objects.get(id = 35)
        resp = f'Articulo: {articulo.titulo}'
    except:
        resp = 'Articulo no encontrado'

    return HttpResponse(resp)

    # Para retornar un objeto JSON desde un modelo de BD

    #articulo = [Articulo.objects.get(id = 35)]
    #dato = serializers.serialize('json', articulo)
    #dato = json.loads(dato)
    
    #return JsonResponse({'Articulo': dato})


def actualizar_articulo(request, id):
    articulo = Articulo.objects.get(pk = id)

    articulo.titulo = 'Acualizado'
    articulo.contenido = 'Fue actualizado'

    articulo.save()

    return HttpResponse(f'Articulo actualizado {articulo.titulo}')

    # dato = serializers.serialize('json', [articulo])
    # dato = json.loads(dato)
    # 
    # return JsonResponse({'Articulo actualizado': dato})


def articulos(request):

    articulos_v = Articulo.objects.filter(publico= True)

    # Obtener objetos 
    #articulos_v = Articulo.objects.all()

    # Ordenar registros
    #articulos_v = Articulo.objects.order_by('titulo') #ordenar
    #articulos_v = Articulo.objects.order_by('-titulo')[0:1] #limitar los elementos #ordenar de forma inversa

    # Agregar filtros o hacer consultas condicionales
    #articulos_v = Articulo.objects.filter(titulo__contains= 'artículo', id__gte = 40) # __contains para busquedas mas flexibles, __exac para busquedas exactas
    # __iexac para buscar mismo contenido pero sin importar si esta en MAYÚSCULAS o minúsculas, __gt mayor que, __gte mayor o igual que, __lt menor que, __lte menor o igual que

    # Excluir registros (consultas condicionales 2)
    #articulos_v = Articulo.objects.filter(titulo__contains = 'Artículo' , publico = False)
    #articulos_v = Articulo.objects.filter(
    #    titulo__contains = 'artículo'
    #).exclude(publico = False) # exlude(condición) para excluir datos

    # SQL en Django
    #articulos_v = Articulo.objects.raw(' SELECT * FROM primeraApp_articulo')

    # OR en consulta
    #articulos_v = Articulo.objects.filter(
    #    #Q(titulo__contains ='2') | Q(titulo__contains ='3') # | or
    #    Q(titulo__contains ='2') | Q(publico = True)
    #)



    return render(request, 'articulos.html', {
        'articulos': articulos_v
    })


def borrar_articulo(request, id):
    articulo = Articulo.objects.get(pk = id)
    articulo.delete()

    return redirect('articulos')


def guardar_articulo(request):

    if request.method == 'GET':

        titulo = request.GET['titulo']
        contenido = request.GET['contenido']
        publico = request.GET['publico']

        if not(titulo or contenido or publico):
            return HttpResponse('<h2>Favor de llenar los campos</h2>')

        articulo = Articulo(
            titulo= titulo,
            contenido= contenido,
            publico= publico
        )

        articulo.save()
    
        return HttpResponse(f'Artículo creado {articulo.titulo} - {articulo.contenido}')

    elif request.method == 'POST':

        titulo = request.POST['titulo'] # ['valor del atributo name en un formulario html']
        contenido = request.POST['contenido']
        publico = request.POST['publico']

        if not(titulo or contenido or publico):
            return HttpResponse('<h2>Favor de llenar los campos</h2>')

        articulo = Articulo(
            titulo= titulo,
            contenido= contenido,
            publico= publico
        )

        articulo.save()
    
        return HttpResponse(f'Artículo creado {articulo.titulo} - {articulo.contenido}')

    else:

        return HttpResponse('<h2>No se pudo crear el articulo</h2>')

  


def crear_articulo_POST(request):
    
    return render(request, 'crear_articulo.html')



def crear_articulo_CLASS(request):

    if request.method == 'POST':
        formulario = FormArticulo(request.POST)

        if formulario.is_valid(): # revisa si el formulario no tiene errores
            datos_form = formulario.cleaned_data # datos del formulario

            titulo = datos_form.get('titulo')
            contenido = datos_form['contenido']
            publico = datos_form['publico']

            articulo = Articulo(
                titulo= titulo,
                contenido= contenido,
                publico= publico
            )

            articulo.save()

            # Crear mensaje flash / sesión flash
            messages.success(request, f'Artículo {articulo.titulo} creado correctamente')

            #return HttpResponse(articulo.titulo + ' - ' + articulo.contenido + ' - ' + articulo.publico)

            return redirect('articulos')

    else:
        formulario = FormArticulo()

    return render(request, 'crear_articulo_CLASS.html', {
        'form': formulario
    })