from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from .models import Alumno

# Create your views here.

def index(request):
    latest_alumno_list = Alumno.objects.order_by('apellido')
    template = loader.get_template('alumnos/index.html')
    context = {
        'latest_alumno_list': latest_alumno_list,
    }
    return HttpResponse(template.render(context, request))

""" # ...
def detail(request, alumno_id):
    alumno = get_object_or_404(Alumno, pk=alumno_id)
    return render(request, 'alumnos/detail.html', {'alumno': alumno})

 """
def detail(request, alumno_id):
    try:
        alumno = Alumno.objects.get(pk=alumno_id)
    except Alumno.DoesNotExist:
        raise Http404("Alumno does not exist")
    return render(request, 'alumnos/detail.html', {'alumno': alumno})

def results(request, alumno_id):
    response = "You're looking at the results of alumno %s."
    return HttpResponse(response % alumno_id)

def vote(request, alumno_id):
    return HttpResponse("You're voting on alumno %s." % alumno_id)