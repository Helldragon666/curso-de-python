

from django.urls import path
from . import views

urlpatterns = [
    path('pagina/<str:dato>', views.pagina, name='pagina')
]