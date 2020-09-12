from django.contrib import admin
from movies.models import Movie, Review

class ReviewInline(admin.TabularInline):
    model = Review

class MovieAdmin(admin.ModelAdmin):
    list_display = ("imdb_id", "title", "year", "imdb_rating")
    inlines = [
        ReviewInline,
    ]
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("pk", "movie", "review_title", "submission_date", "author_rating", "contains_spoilers")

admin.site.register(Movie, MovieAdmin)
admin.site.register(Review, ReviewAdmin)
