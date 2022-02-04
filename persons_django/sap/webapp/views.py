from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from personas.models import Persona

def bienvenido(request):
    var_num_personas = Persona.objects.count()
    personas = Persona.objects.all()
    return render(request, 'home.html', {'num_personas': var_num_personas, 'personas': personas})

