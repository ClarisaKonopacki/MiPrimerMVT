from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from .models import Persona

def index(request):
    personas = Persona.objects.all()
    context = {'clase': 'Mi primer App', 'personas' : personas}
    return render(request,"familia_lista.html", context)

# Create your views here.
