from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    class_num = models.CharField(max_length=5)
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.user.email