from django.shortcuts import render

from .models import Teacher, ClassRoom

# Create your views here.
def index(req):
    return render(req, 'main/main.html')

def maps(req):
    return render(req, 'maps/index.html')

def map_search(req):
    if req.method == 'POST':
        searched = req.POST['searched']
        map_list = ClassRoom

def teachers(req):
    teacherlist = Teacher.objects.all()

    return render(req, 'teachers/teachers.html', {'techerlsit' : teacherlist})

def science(req):
    return render(req, 'science/science.html')

def login(require):
    return render(require, 'login/login.html')

def signup(require):
    return render(require, 'signup/signup.html')

def trans_edu(require):
    return render(require, 'trans_edu/trans_edu.html')