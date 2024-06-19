from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ImageModelSerializer
from .models import Image, ClassRoom, Teacher
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ImageModelFilter
from django.http import JsonResponse

class ImageModelViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ImageModelFilter


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
        images = Image.objects.all()
        
        return render(req,'maps/map_search.html' ,{'searched':searched, 'map_list':map_list, 'images':images})
    
    else:
        return render(req,'maps/map_search.html', {})
    
def building_details(req):
    building = req.GET.get('building')
    details = ClassRoom.objects.filter(location__icontains=building)
    detail_list = list(details.values('name', 'location', 'loc_num'))
    return JsonResponse(detail_list, safe=False)

def teachers(req):
    teacherlist = Teacher.objects.all()

    return render(req, 'teachers/teachers.html', {'techerlist' : teacherlist})

def search_teachers(req):
    query = req.GET.get('q', '')
    teachers = Teacher.objects.filter(name__icontains=query)
    teacher_list = list(teachers.values('name', 'subject', 'location', 'profile_img', 'introduce'))
    return JsonResponse(teacher_list, safe=False)

def science(req):
    return render(req, 'science/science.html')

def login(require):
    return render(require, 'login/login.html')

def signup(require):
    return render(require, 'signup/signup.html')

def trans_edu(require):
    return render(require, 'trans_edu/trans_edu.html')