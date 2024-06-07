from django.shortcuts import render

# Create your views here.
def login(require):
    return render(require, 'login/login.html')

def signup(require):
    return render(require, 'signup/signup.html')