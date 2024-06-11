from django.shortcuts import render

from .models import Teacher, ClassRoom, Image

# Create your views here.
def index(req):
    return render(req, 'main/main.html')

def maps(req):
    return render(req, 'maps/index.html')

def map_search(req):
    if req.method == 'POST':
        searched = req.POST['searched']
        searched_txt = str(searched)
        searched_txt = searched.replace(' ', '')
        searched_txt = searched_txt.replace('학년','-')
        searched_txt = searched_txt.replace('반', '')
        print(searched_txt)
        
        map_list1 = ClassRoom.objects.filter(name__icontains=searched_txt)
        map_list2 = ClassRoom.objects.filter(location__icontains=searched_txt)
        map_list = map_list1 | map_list2
        print(map_list)
        images = []
        for maps in map_list:
            sel = maps.loc_num
            sel = str(sel)
            print(sel)
            # images.append(Image.objects.get(loc_num=sel))
        
        return render(req,'maps/map_search.html' ,{'searched':searched, 'map_list':map_list, 'images':images})
    
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