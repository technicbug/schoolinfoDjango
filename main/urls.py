from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'images', ImageModelViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('maps/', maps, name  = 'maps'),
    path('map/search/', map_search, name='map_search'),
    path('science/', science, name = 'science'),
    path('teachers/', teachers, name = 'teachers'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('trans_edu/', trans_edu, name='trans_edu'),
    path('getmap/', include(router.urls)),
]