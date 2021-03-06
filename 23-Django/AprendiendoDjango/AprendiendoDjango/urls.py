"""AprendiendoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings

from primeraApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'), # ruta /
    path('ruta-1/', views.hola_mundo, name='ruta_1'),
    path('pagina-prueba/', views.pagina, name='pagina'),
    path('pagina-prueba/<int:redirigir>', views.pagina, name='pagina'),
    path('contacto/', views.contacto, name='contacto'),
    # contacto/yon/
    path('contacto/<str:nombre>/', views.contacto, name='contacto'),
    path('contacto/<str:nombre>/<str:apellido>', views.contacto, name='contacto'),
    path('crear-articulo/<str:titulo>/<str:contenido>/<str:publico>', views.crear_articulo, name='crear_articulo'),
    path('articulo/', views.articulo, name='articulo'),
    path('actualizar-articulo/<int:id>', views.actualizar_articulo),
    path('articulos/', views.articulos, name='articulos'),
    path('borrar-articulo/<int:id>', views.borrar_articulo, name='borrar'),
    path('guardar_articulo/', views.guardar_articulo, name='guardar'),
    path('crear-articulo-post/', views.crear_articulo_POST, name='crear'),
    path('crear-articulo-CLASS/', views.crear_articulo_CLASS, name='crearCLASS')
]


# Configuración para cargar Imágenes o Ficheros (Archivos)
if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
