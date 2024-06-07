from django.contrib import admin
from main.models import Teacher, ClassRoom, Image
from .models import User

admin.site.register(User)
admin.site.register(Teacher)
admin.site.register(ClassRoom)
admin.site.register(Image)