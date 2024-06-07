from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    class_num = models.CharField(max_length=5, blank=False)
    
