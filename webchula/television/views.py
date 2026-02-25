from django.shortcuts import render
from television import models as md

# Create your views here.
def index(request):
    return render(request, 'index.html')

def series(request):
    service = md.ServiceSeries()
    listaseries = service.getSeries()
    informacion = {
        "listaseries": listaseries
    }
    return render(request, "series.html", informacion)

def personajes(request):
    if ('idSerie' in request.GET):
       service = md.ServiceSeries()
       listapersonajes = service.getPersonajesSerie(int(request.GET['idSerie']))
       informacion = {
          'listapersonajes': listapersonajes
       }
       return render(request, "personajes.html", informacion)
    else:
       return render(request, "personajes.html")
    
def insertarpersonaje(request):
    servicio = md.ServiceSeries()
    listaSeries = servicio.getSeries()
    informacion = {
        "listaseries": listaSeries
    }    
    if ('cajaid' in request.POST):
        servicio.insertarPersonaje(
            int(request.POST['cajaid']),
            request.POST['cajanombre'],
            request.POST['cajaimagen'],
            int(request.POST['cajaidserie'])
        )
        return render(request, "insertarpersonaje.html", informacion)
    else:
        return render(request, "insertarpersonaje.html", informacion)





