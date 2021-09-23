from django.contrib import admin
from .models import Pagina

# Register your models here.

admin.site.register(Pagina)


titulo = 'Proyecto con Django'
subtitulo = 'Panel de Gestión'

admin.site.site_header = titulo
admin.site.site_title = titulo
admin.site.index_title = subtitulo

