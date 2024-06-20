from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from .models import CustomUser
import re

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'name', 'class_num', 'password1', 'password2')
        labels = {
            'name': '이름',  # 원하는 레이블 내용으로 수정
            'class_num': '학번',  # 원하는 레이블 내용으로 수정
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        pattern = r'^yangil\.s\d{6}@ggh\.goe\.go\.kr$'
        if not re.match(pattern, email):
            raise forms.ValidationError('학교에서 지급된 이메일을 사용해야합니다')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('이미 가입 완료된 이메일 입니다.')
        return email

class CustomUserLoginForm(AuthenticationForm):
    username = forms.EmailField(label='이메일', widget=forms.EmailInput(attrs={'autofocus': True}))


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'class_num']
        widgets = {
            'name': forms.TextInput(attrs={'id': 'name', 'class': 'profile-update-form-control'}),
            'class_num': forms.TextInput(attrs={'id': 'class_num', 'class': 'profile-update-form-control'}),   
        }
        labels = {
            'name': '이름',  # 원하는 레이블 내용으로 수정
            'class_num': '학번',  # 원하는 레이블 내용으로 수정
        }

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        

        
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'name', 'class_num', 'password1', 'password2')
        labels = {
            'email': '이메일',
            'name': '이름',  # 원하는 레이블 내용으로 수정
            'class_num': '학번',  # 원하는 레이블 내용으로 수정
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        pattern = r'^yangil\.s\d{6}@ggh\.goe\.go\.kr$'
        if not re.match(pattern, email):
            raise forms.ValidationError('학교에서 지급된 이메일을 사용해야 합니다')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('이미 가입 완료된 이메일 입니다.')
        return email

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'name', 'class_num')