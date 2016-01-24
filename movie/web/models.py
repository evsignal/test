from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Actor(models.Model):
    name = models.CharField(max_length=50)
    real_name = models.CharField(max_length=50, null=True)
    biography = models.TextField(null=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=50)
    review = models.TextField()
    actors = models.ManyToManyField(Actor, related_name="actor_movies")

    def __str__(self):
        return self.title



