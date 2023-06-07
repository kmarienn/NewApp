from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

from personas.models import Persona
# Create your views here.
def bienvenida (request):
    #print('Hola')
    #return HttpResponse ('<!DOCTYPE html><html><head><title></title><body><p>Hola Mundo de Django</p></body></head></html>')
    pagina = loader.get_template('saludo.html')
    return HttpResponse(pagina.render())
def hola (request, nombre):
    apellido = request.GET ['apellido']
    nivel = request.GET['nivel']
    curso = request.GET['curso']
    nombreCompleto = nombre + ' ' + apellido
    datos = {'nombre': nombreCompleto, 'curso': curso, 'nivel': nivel}
    pagina = loader.get_template('saludo.html')
    return HttpResponse (pagina.render(datos, request))

def edad(request, edad):
    pagina = loader.get_template('edad.html')
    mensaje = {'edad': edad }
    return HttpResponse(pagina.render(mensaje, request))

def registro(request):
    cantidad_personas = Persona.objects.count()
    personas = Persona.objects.all().values()

    nombres = list ()
    for persona in personas:
        #print(persona)
        nombres.append(persona['nombre'] + ' ' + persona['apellido'])

    datos = {'cantidad': cantidad_personas, 'personas':personas, 'nombres': nombres}
    pagina = loader.get_template('personas.html')
    return HttpResponse(pagina.render(datos, request))