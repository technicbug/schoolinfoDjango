from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags


from .forms import CustomUserCreationForm, CustomUserLoginForm, ProfileUpdateForm
from .models import CustomUser




def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = request.get_host()
            mail_subject = '[2024 양일고 프로젝트 봉사활동] 이메일 인증을 완료해주세요'
            message = render_to_string('signup/activation_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            text_content = strip_tags(message)
            to_email = form.cleaned_data.get('email')
            # send_mail(mail_subject, message, 'yangilinfoproject@gmail.com', [to_email])
            msg = EmailMultiAlternatives(mail_subject, text_content, 'yangilinfoproject@gmail.com', [to_email])  # EmailMultiAlternatives 사용
            msg.attach_alternative(message, "text/html")  # HTML 버전의 메시지 추가
            msg.send()
            return render(request, 'signup/email_verification_sent.html')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup/signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('index')
    else:
        return render(request, 'signup/activation_invaild.html')




def login_view(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # 로그인 성공 후 리다이렉트할 경로
    else:
        form = CustomUserLoginForm()
    return render(request, 'login/login.html', {'form': form})


@login_required
def profile_view(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'profile/profile.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('index')



