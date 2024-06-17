from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignUpForm
from django.http import JsonResponse
from .models import UserProfile
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
           

            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            name = request.POST.get('name')  # 사용자 이름 가져오기
            class_num = request.POST.get('class_num')  # 클래스 번호 가져오기
            email = request.POST.get('email')

            UserProfile.objects.create(user=user, name=name, class_num=class_num, email=email)

           
            auth_login(request, user)
            return redirect('index')
        else:
            print('Form is invalid')
            print(form.errors)  # 폼의 오류 메시지를 출력
    else:
        form = SignUpForm()
        print('here')
    return render(request, 'signup/signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.email, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Invalid credentials')
        except User.DoesNotExist:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login/login.html')

def check_email(request):
    email = request.GET.get('email', None)
    data = {
        'is_taken': User.objects.filter(email=email).exists()
    }
    return JsonResponse(data)

@login_required
def logout_page(request):
    user_profile = None
    if request.user.is_authenticated:
        try:
            user_profile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:

            user_profile = None

    return render(request, 'logout/logout.html', {
        'user_profile': user_profile
    })

@login_required
def edit_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save(request.user)
            return redirect('accounts:logout_page')
    else:
        form = UserProfileForm(instance=user_profile)
    
    return render(request, 'accounts/edit_profile.html', {
        'form': form,
        'email': request.user.email
    })