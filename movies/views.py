import json
import logging
import re
import sys
from pathlib import Path

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.db.models import Q
from django.shortcuts import HttpResponse, redirect, render, reverse
from django.views.generic import DetailView, ListView

from movies.models import Movie
from movies_collector.imdb_collector import (get_movie_details,
                                             get_top_rated_movies,
                                             search_movies, url_exists)
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
    login_url = "account_login"
    permission_required = "movies.paid_for_membership"

    @staticmethod
    def store_movie(movie_details):
        poster_url = movie_details.get("Poster")
        Movie(
            imdb_id=movie_details.get("imdbID"),
            title=movie_details.get("Title"),
            year=int(movie_details.get("Year")),
            plot=movie_details.get("Plot"),
            poster_url=poster_url if url_exists(poster_url) else None,
            imdb_rating=movie_details.get("imdbRating"),
            full_json_details=json.dumps(movie_details),
        ).save()

    # @login_required
    @staticmethod
    def toggle_seen(request, pk):
        movie = Movie.objects.get(pk=pk)

        user = request.user
        if movie.watched_by.filter(pk=user.pk).exists():
            movie.watched_by.remove(user)
            seen = False
        else:
            movie.watched_by.add(user)
            seen = True

        return render(request, 'movies/movie_detail.html', {'movie': movie, 'seen': seen})

class SearchResultsListView(ListView):
    model = Movie
    template_name = "movies/movie_list.html"
    context_object_name = "movies"

    def get_queryset(self):
        search_term = self.request.GET.get("q")
        log.warning(f"Searching movies: {search_term}")

        found_ids = [x["imdbID"] for x in search_movies(search_term)]
        log.warning(f"Matching IDs: {', '.join(found_ids)}")

        for imdb_id in found_ids:
            if not Movie.objects.filter(pk=imdb_id).exists():
                movie_details = get_movie_details(imdb_id)
                log.warning(f"Fetched movie details: {movie_details}")

                try:
                    MovieDetailView.store_movie(movie_details)
                except Exception as e:
                    log.error(f"/!\ Unable to save the following movie details /!\ \n{e}")
                    log.error(json.dumps(movie_details))

        return Movie.objects.filter(Q(title__icontains=search_term))
