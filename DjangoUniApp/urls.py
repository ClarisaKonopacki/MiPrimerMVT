from django.urls import path 
from DjangoUniApp.views import index, agregar,borrar, buscar, form_carga

urlpatterns =[
    path('', index, name='index'),
    path('agregar/', agregar, name="agregar"),
    path('borrar/<identificador>', borrar, name="borrar"),
    path('buscar/', buscar, name="buscar"),
    path('form_carga/', form_carga),
        ]