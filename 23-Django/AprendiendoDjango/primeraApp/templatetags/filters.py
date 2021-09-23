
# Filtros personalizados

from django import template

register = template.Library()

@register.filter(name='saludo')

def saludo(value):

    texto = ''

    if len(value) >= 8:
        texto = 'tu nombre es muy largo'

    return f'''<h1 style="background:green;color:white;">HOLI {value} ;33</h1>
                <p>{texto}</p>
            '''
     