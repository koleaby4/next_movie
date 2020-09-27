import uuid

from django.db import models

from movies.models import Movie
from users.models import CustomUser


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    watched_movies = models.ManyToManyField(Movie, blank=True, null=True)
    watched_movies_average_rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    watched_movies_genres = models.JSONField(default=None, blank=True, null=True)

    def __str__(self):
        return f"""
        Profile details:
            User {self.user}
            watched_movies_average_rating: {self.watched_movies_average_rating}
            watched_movies_genres: {self.watched_movies_genres}"""
