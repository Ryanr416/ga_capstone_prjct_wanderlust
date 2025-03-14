from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Destinations(models.Model):
    name = models.CharField(max_length=250)
    country = models.CharField(max_length=60)
    language = models.CharField(max_length=100)
    currency = models.CharField(max_length=3)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('destinations_detail', kwargs={'pk': self.id})
    
class Trips(models.Model):
    name = models.CharField(max_length=250)
    startDate = models.DateField(null=True)
    endDate = models.DateField(null=True)
    budget = models.IntegerField(null=True)
    destination_ids = models.ManyToManyField(Destinations, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('trips_detail', kwargs={'trip_id': self.id})

    class Meta: 
        ordering = ['-startDate']

class Checklist(models.Model):
    todos = models.CharField(max_length=250)
    complete = models.BooleanField()
    trip = models.ForeignKey(Trips, on_delete=models.CASCADE)

class Travelers(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trips, on_delete=models.CASCADE)

class Activities(models.Model):
    plannedAct = models.CharField(max_length=250)
    endDate = models.DateField()
    dueDate = models.DateField()
    trip = models.ForeignKey(Trips, on_delete=models.CASCADE)

class Photos(models.Model):
    url = models.CharField(max_length=200)
    destination_id = models.ForeignKey(Destinations, on_delete=models.CASCADE)
