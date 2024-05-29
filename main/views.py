from django.shortcuts import render

from .models import Teachers

# Create your views here.
def index(req):
    return render(req, 'main/index.html')

def maps(req):
    return render(req, 'maps/insdex.html')


def techers(req):
    teacherlist = Teachers.objects.all()

    return render(req, 'techers/techers.html', {'techerlsit' : teacherlist})

