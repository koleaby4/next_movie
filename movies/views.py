import json
import logging
import re
import sys
from pathlib import Path

from django.shortcuts import HttpResponse, render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from movies.models import Movie
from movies_collector.imdb_collector import get_movie_details, get_top_rated_movies
from utils.utilities import get_secret

log = logging.getLogger(__name__)


class MovieListView(ListView):
    model = Movie
    template_name = "movies/movie_list.html"
    context_object_name = "movies"


class MovieDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Movie
    template_name = "movies/movie_detail.html"
    context_object_name = "movie"
    login_url = 'account_login'
    permission_required = 'movies.paid_for_membership'




def index(request):

    for movie in get_top_rated_movies():
        movie_id = re.search(r"(?<=/title/)\w+", movie["id"])[0]
        try:
            Movie.objects.get(imdb_id=movie_id)
        except Movie.DoesNotExist as e:
            log.info(f"Movie {movie_id} not found in DB - fetching details...")
            movie_details = get_movie_details(movie_id)
            store_movie(movie_details)

    context = {"movies": Movie.objects.all()}

    return render(request, "index.html", context=context)


def store_movie(movie_details):
    Movie(
        imdb_id=movie_details.get("imdbID"),
        title=movie_details.get("Title"),
        year=int(movie_details.get("Year")),
        plot=movie_details.get("Plot"),
        poster_url=movie_details.get("Poster"),
        imdb_rating=movie_details.get("imdbRating"),
        full_json_details=json.dumps(movie_details),
    ).save()


def about(request):
    return render(request, "about.html")
