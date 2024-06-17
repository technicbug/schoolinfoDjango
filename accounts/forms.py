from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import UserProfile


class SignUpForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label='이름', required=True)
    class_num = forms.CharField(max_length=5, label='학번', required=True)
    password = forms.CharField(widget=forms.PasswordInput, label='비밀번호', required=True)
    password2 = forms.CharField(widget=forms.PasswordInput, label='비밀번호 재확인', required=True)

    class Meta:
        model = User
        fields = ['email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('비밀번호가 일치하지 않습니다')
        return cd['password2']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('이 이메일은 이미 사용중 입니다')
        return email

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.username = self.cleaned_data['email']  # 이메일을 username으로 사용
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    

class UserProfileForm(forms.ModelForm):
    class_num = forms.CharField(max_length=5, required=True)
    name = forms.CharField(max_length=100, required=True)

    class Meta:
        model = UserProfile
        fields = ['class_num', 'name']
    
    def save(self, user, commit=True):
        profile = super(UserProfileForm, self).save(commit=False)
        profile.user = user
        if commit:
            profile.save()
        user.save()
        return profile