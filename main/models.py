from django.db import models

# Create your models here.
class Teacher(models.Model):

    name = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    profile_img = models.ImageField(blank= True, upload_to = 'images/')

    def __str__(self):
        return self.name
    
class ClassRoom(models.Model):

    name = models.CharField(max_length=30)
    location = models.CharField(blank=True, max_length=30)
    loc_num = models.CharField(blank=True, max_length=10)
    def __str__(self):
        return self.name