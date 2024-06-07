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
        searched = str(searched)
        searched = searched.replace(' ', '')
        searched = searched.replace('학년','-')
        searched = searched.replace('반', '')
        map_list1 = ClassRoom.objects.filter(name__contains=searched)
        map_list2 = ClassRoom.objects.filter(location__contains=searched)
        map_list = map_list1 + map_list2
        return render(req,'maps/map_search.html' ,{'searched':searched, 'maplist':map_list})
    
    else:
        return render(req,'maps/map_search.html', {})

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