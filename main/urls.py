from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('maps/', maps),
    path('science/', science),
    path('teachers/', teacher),

]