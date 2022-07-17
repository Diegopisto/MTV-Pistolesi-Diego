from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
# Create your views here.

from familiamtv.models import Familia

def familia(self, nombre, parentezco, edad):

    familia = Familia(nombre=nombre, parentezco=parentezco, edad=edad)
    familia.save()

    return HttpResponse(f"""<p>Nombre: {familia.nombre} - Parentezco: {familia.parentezco} - Edad: {familia.edad} </p>""")





def comosellaman(request):

    lista_nombres = ["Sonia","Eduardo","Olga"]

    diccionario = {"nombress":lista_nombres}

    plantilla = loader.get_template("templates.html")

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)
 
