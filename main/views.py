from django.shortcuts import render

from .models import Teacher, ClassRoom

# Create your views here.
def index(req):
    return render(req, 'main/main.html')

def maps(req):
    return render(req, 'maps/index.html')


def teachers(req):
    teacherlist = Teacher.objects.all()

    return render(req, 'teachers/teachers.html', {'techerlsit' : teacherlist})

def science(req):
    return render(req, 'science/science.html')
