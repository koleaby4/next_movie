from django.contrib import admin
from movies.models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ("imdb_id", "title", "year", "imdb_rating")

admin.site.register(Movie, MovieAdmin)
