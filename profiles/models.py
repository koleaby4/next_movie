from django.db import models

from users.models import CustomUser
from movies.models import Movie


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    watched_movies = models.ManyToManyField(Movie, blank=True, null=True)
