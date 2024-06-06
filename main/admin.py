from django.contrib import admin

# Register your models here.
from .models import Teacher, ClassRoom, Image

admin.site.register(Teacher)
admin.site.register(ClassRoom)
admin.site.register(Image)