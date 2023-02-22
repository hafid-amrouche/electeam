from django.db import models

# Create your models here.

class INFO(models.Model):
    welcome = models.TextField()
    description = models.TextField()
    main_image = models.ImageField()
    video = models.FileField()

class Service(models.Model):
    title = models.CharField(max_length=50)
    paragraph = models.TextField()

class ServiceImage(models.Model):
    service = models.ForeignKey('Service', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='services/')

class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gellery/')

class ContactUs(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    fname = models.CharField(max_length=50)
    email = models.TextField(max_length=50)
    message = models.TextField(max_length=1000)