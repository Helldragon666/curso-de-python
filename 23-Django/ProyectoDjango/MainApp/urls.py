

from django.urls import path
#from MainApp import views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]