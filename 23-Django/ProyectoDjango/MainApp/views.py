from django.shortcuts import render

# Create your views here.


def index(request):
    
    return render(request, 'MainApp/index.html', {
        'titulo': 'Inicio'
    })


def about(request):
    
    return render(request, 'MainApp/about.html', {
        'titulo': 'Sobre Nosotros'
    })