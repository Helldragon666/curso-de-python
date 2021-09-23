from django.contrib import admin

from .models import Articulo, Categoria

# Register your models here.

class ArticuloAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Categoria)
#admin.site.register([Articulo, Categoria])

# Configurar el Título del panel de administración
titulo = 'Master en Python (Django)'
admin.site.site_header = titulo
admin.site.site_title = titulo
admin.site.index_title = 'Panel de Gestión'
