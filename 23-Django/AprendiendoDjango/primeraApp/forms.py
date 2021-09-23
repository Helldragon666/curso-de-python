


from django import forms
from django.core import validators


class FormArticulo(forms.Form):
    titulo = forms.CharField(
        label='Título',
        #initial='Título del artículo' # para dar un valor inicial
        widget=forms.TextInput({'placeholder': 'Título del artículo'}),
        max_length=40,
        #required=True
        validators=[
            validators.MinLengthValidator(4, 'El título es demasiado corto'),
            validators.RegexValidator('^[A-Za-z0-9ñ ]*$', 'Caracteres no válidos', '400')
        ]
    )
    contenido = forms.CharField(
        label='Contenido',
        widget=forms.Textarea(attrs={'placeholder': 'Contenido del artículo'}),
        #initial='Contenido del artículo'
        validators= [
            validators.MaxLengthValidator(20, 'Solo se permiten 20 cracteres como máximo')
        ]   
    )

    publico_opciones =[
        ('', 'Seleccione'),
        (1, 'Publico'), # tupla ('value', opción que se muestra)
        (0, 'Privado')
    ]

    publico = forms.TypedChoiceField(
        label='Elige una opción',
        choices = publico_opciones
    )

    #publico.widget.attrs.update({
    #    'placeholder': 'Contenido del artículo'
    #})