from django.contrib import admin

# Register your models here.
from .models import Teacher, ClassRoom

admin.site.register(Teacher)
admin.site.register(ClassRoom)