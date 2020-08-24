from django.contrib import admin
from movies.models import Movie, Review

class ReviewInline(admin.TabularInline):
    model = Review

class MovieAdmin(admin.ModelAdmin):
    list_display = ("imdb_id", "title", "year", "imdb_rating")
    inlines = [
        ReviewInline,
    ]

admin.site.register(Movie, MovieAdmin)
