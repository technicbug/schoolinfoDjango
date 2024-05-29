from django.db import models

# Create your models here.
class Teachers(models.Model):

    name = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    profile_img = models.ImageField(blank= True, upload_to = 'images/')

    def __str__(self):
        return self.name