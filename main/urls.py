from django.urls import path, include
from .views import ImageModelViewSet
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from .views import *

router = DefaultRouter()
router.register(r'images', ImageModelViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('maps/', maps, name='maps'),
    path('map/search/', map_search, name='map_search'),
    path('science/', science, name='science'),
    path('teachers/', teachers, name='teachers'),
    path('search_teachers/', search_teachers, name='search_teachers'),
    path('trans_edu/', trans_edu, name='trans_edu'),
    path('getmap/', include(router.urls)),  # API URL 패턴 포함
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

