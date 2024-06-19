from django.urls import path, include
from .views import *
from rest_framework import urls
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns =[

    path('login/', login_view, name='login'),
    path('profile/', profile_view, name='profile'),
    path('logout/', logout_view, name='logout'),

    # path('csregister/', views.cs_register_view, name='csregister'),
    path('signup/', signup, name='signup'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),

 ]

