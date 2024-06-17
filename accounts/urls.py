from django.urls import path, include
from .views import *
from rest_framework import urls
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns =[
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('check-email/', check_email, name='check_email'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout_page/', logout_page, name='logout_page'),  # 로그아웃 폼 페이지
 ]

