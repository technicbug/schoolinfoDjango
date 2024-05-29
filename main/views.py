from django.shortcuts import render

from .models import Teachers

# Create your views here.
def index(req):
    return render(req, 'main/index.html')

def maps(req):
    return render(req, 'maps/index.html')


def techers(req):
    teacherlist = Teachers.objects.all()

    return render(req, 'teachers/techers.html', {'techerlsit' : teacherlist})

def science(req):
    return render(req, 'science/science.html')
