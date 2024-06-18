from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from .models import CustomUser
import re

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'name', 'class_num', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        pattern = r'^yangil\.s\d{6}@ggh\.goe\.go\.kr$'
        if not re.match(pattern, email):
            raise forms.ValidationError('학교에서 지급된 이메일을 사용해야합니다')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('이미 가입 완료된 이메일 입니다.')
        return email

class CustomUserLoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'autofocus': True}))


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'class_num', 'password']

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['password'].required = False
        self.fields['password'].widget = forms.PasswordInput()

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password:
            return password
        else:
            return self.instance.password
        
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'name', 'class_num', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        pattern = r'^yangil\.s\d{6}@ggh\.goe\.go\.kr$'
        if not re.match(pattern, email):
            raise forms.ValidationError('Email must start with yangil.s followed by 6 digits and end with @ggh.goe.go.kr')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already registered.')
        return email

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'name', 'class_num')