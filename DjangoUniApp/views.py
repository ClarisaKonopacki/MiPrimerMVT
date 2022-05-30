from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render
from django.template import loader
from DjangoUniApp.forms import PersonaForm, BuscarPersonasForm
from .models import Persona

#def index(request):
   # personas = Persona.objects.all()
   # context = {'clase': 'Mi primer App', 'personas' : personas}
   # return render(request,"familia_lista.html", context)

def index(request):
    personas = Persona.objects.all()
    template = loader.get_template('familia_lista.html')
    context = {
        'personas': personas,
    }
    return HttpResponse(template.render(context, request))

def form_carga(request):
    
    return render(request, "form_carga.html")


def agregar(request):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la persona fue cargada con éxito
    '''

    if request.method == "POST":
        form = PersonaForm(request.POST)
        if form.is_valid():

            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            edad = form.cleaned_data['edad']
            Persona(nombre=nombre, apellido=apellido, email=email, fecha_nacimiento=fecha_nacimiento, edad=edad).save()

            return HttpResponseRedirect("/")
    elif request.method == "GET":
        form = PersonaForm()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")

    
    return render(request, 'DjangoUniApp/form_carga.html', {'form': form})


def borrar(request, identificador):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la persona fue eliminada con éxito        
    '''
    if request.method == "GET":
        persona = Persona.objects.filter(id=int(identificador)).first()
        if persona:
            persona.delete()
        return HttpResponseRedirect("/DjangoUniApp/")
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")


def actualizar(request, identificador):
    '''
    TODO: implementar una vista para actualización
    '''
    pass


def buscar(request):
    if request.method == "GET":
        form_busqueda = BuscarPersonasForm()
        return render(request, 'form_busqueda.html', {"form_busqueda": form_busqueda})

    elif request.method == "POST":
        form_busqueda = BuscarPersonasForm(request.POST)
        if form_busqueda.is_valid():
           palabra_a_buscar = form_busqueda.cleaned_data['palabra_a_buscar']
           personas = Persona.objects.filter(nombre__icontains=palabra_a_buscar)

        return  render(request, 'lista_familiares.html', {"personas": personas})
