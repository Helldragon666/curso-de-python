from django.db import models

# Create your models here.

class Articulo(models.Model): # models.Model para identificarlo como Modelo
        titulo     = models.CharField(max_length=40, verbose_name='título') #CharField() campo de caracteres
        contenido  = models.TextField() #TextField() campo de texto
        imagen     = models.ImageField(default='null', upload_to='articulos')
        publico    = models.BooleanField()
        created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
        updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

        class Meta: # Para la visualización en el Panel de Administración de Django 
                verbose_name = 'Artículo'
                verbose_name_plural = 'Artículos' 
                #ordering = ['-id'] #ordenar por id

        def __str__(self):
            
            if self.publico:
                texto = 'publico'
            else:
                texto = 'privado'
                
            return f'{self.titulo} ({texto})'
        

        

class Categoria(models.Model):
        nombre      = models.CharField(max_length=40)
        descripcion = models.CharField(max_length=150)
        created_at  = models.DateField()

        class Meta:
                verbose_name = 'Categoría'
                verbose_name_plural = 'Categorías'


        