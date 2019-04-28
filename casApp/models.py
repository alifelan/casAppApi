from django.db import models

# Create your models here.


class Casa(models.Model):
    name = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=50)
    date = models.DateTimeField()


class Location(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    maps = models.CharField(max_length=400)
    photo = models.CharField(max_length=400)


class User(models.Model):
    name = models.CharField(max_length=50)
    mat = models.CharField(max_length=9, primary_key=True)
    password = models.CharField(max_length=50)
    casa = models.ForeignKey(to=Casa, related_name="users", on_delete=models.CASCADE)
    events = models.ManyToManyField(to=Event, related_name="events")
