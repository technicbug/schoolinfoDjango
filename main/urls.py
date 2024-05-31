from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('maps/', maps, name  = 'maps'),
    path('science/', science, name = 'science'),
    path('teachers/', teachers, name = 'teachers'),
]