from django.db import models


class Developer(models.Model):
    full_name = models.CharField(max_length=50)
    speciality = models.CharField(max_length=150) 
    image = models.ImageField(upload_to='dev_images/')