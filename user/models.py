from django.db import models


# Create your models here.
class AddEvent(models.Model):
    title = models.CharField(max_length=100,default="")
    description = models.CharField(max_length=500,default="")
    date = models.CharField(max_length=100,default=False)
    place = models.CharField(max_length=100,default="")
    image = models.FileField( upload_to='photos')
class ImageUpload(models.Model):
    images = models.FileField( upload_to='gallery')
    # images1 = models.FileField( upload_to='gallery')

class Loging(models.Model):
    username = models.CharField(max_length=45,default="")
    password = models.CharField(max_length=45,default=False)
