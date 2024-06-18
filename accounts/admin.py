from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser
# from .forms import CustomUserCreationForm, CustomUserChangeForm

@admin.register(CustomUser)
class PersonAdmin(admin.ModelAdmin):
    pass