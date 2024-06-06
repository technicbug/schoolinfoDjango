from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('maps/', maps, name  = 'maps'),
    path('map/search/', map_search, name='map_search'),
    path('science/', science, name = 'science'),
    path('teachers/', teachers, name = 'teachers'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('trans_edu/', trans_edu, name='trans_edu'),
]