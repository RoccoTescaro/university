from django.db import models
from django.contrib.auth.models import User

class Venue(models.Model):
    name = models.CharField(max_length=127)
    address = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=15)
    phone = models.CharField(max_length=12, blank=True)
    web = models.URLField(blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name 
    
class MyUser(models.Model):
    first_name = models.CharField(max_length=23)
    last_name = models.CharField(max_length=23)
    email = models.EmailField()
    

    def __str__(self):
        return self.first_name + " " + self.last_name 

class Event(models.Model):
    name = models.CharField(max_length=127)
    date = models.DateTimeField()
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(MyUser, blank=True)

    def __str__(self):
        return self.name