import uuid

from django.db import models

from movies.models import Movie
from users.models import CustomUser


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    watched_movies = models.ManyToManyField(Movie, blank=True, null=True)
