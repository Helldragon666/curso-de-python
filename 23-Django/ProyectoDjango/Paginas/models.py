from django.db import models

# Create your models here.

class Pagina(models.Model):
    titulo     = models.CharField(max_length=50, verbose_name='Título')
    contenido  = models.TextField(verbose_name='Contenido')
    slug       = models.CharField(unique=True, max_length=150, verbose_name='URL amigable')
    visible    = models.BooleanField(verbose_name='Visible')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'

    def __str__(self):
        return self.titulo
    
