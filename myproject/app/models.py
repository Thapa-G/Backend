
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

#class ImageUpload(models.Model):
 #   image = models.ImageField(upload_to='images/')
   
class ImageUpload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Associate image with a user
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return f"{self.user.username} - {self.image.name}"