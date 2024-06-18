from django.urls import path, include
from .views import *
from rest_framework import urls
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns =[
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('profile/', profile_view, name='profile'),
    path('logout/', logout_view, name='logout'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('email_verification_sent/', email_verification_sent, name='email_verification_sent'),
 ]

