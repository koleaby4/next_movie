import json
import logging
import re
import sys
from pathlib import Path

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.shortcuts import HttpResponse, redirect, render, reverse
from django.views.generic import DetailView, ListView

from movies.models import Movie, Review  # , LatestMovie
from movies_collector.imdb_collector import (
    get_movie_details,
    get_movie_reviews,
    get_top_rated_movies,
    search_movies,
    url_exists,
    get_now_playing_imdb_ids
)
from utils.utilities import get_secret

log = logging.getLogger(__name__)


class MovieListView(ListView):
    model = Movie
    template_name = "movies/movies.html"
    context_object_name = "movies"

    def get_queryset(self):
        results = []

        for imdb_id in get_top_rated_movies():
            if not Movie.objects.filter(pk=imdb_id).exists():
                movie = persist_movie(imdb_id)
                results.append(movie)
            else:
                results.append(Movie.objects.get(pk=imdb_id))

        return results


class MovieDetailView(LoginRequiredMixin, DetailView):
    model = Movie
    template_name = "movies/movie_detail.html"
    context_object_name = "movie"
    login_url = "account_login"
    permission_required = "movies.paid_for_membership"

    @staticmethod
    def toggle_watched(request, pk):
        movie = Movie.objects.get(pk=pk)

        user = request.user

        if movie.watched_by.filter(pk=user.pk).exists():
            movie.watched_by.remove(user)
        else:
            movie.watched_by.add(user)

        movie.save()

        return redirect(reverse("movie_detail", args=[movie.pk]))


class SearchResultsListView(ListView):
    model = Movie
    template_name = "movies/movies.html"
    context_object_name = "movies"

    def get_queryset(self):

        search_term = self.request.GET.get("q")
        log.warning(f"Searching movies: {search_term}")

        found_ids = [x["imdbID"] for x in search_movies(search_term)]
        log.warning(f"Matching IDs: {', '.join(found_ids)}")

        for imdb_id in found_ids:

            if not Movie.objects.filter(pk=imdb_id).exists():
                movie = persist_movie(imdb_id)

        # ToDo: change to pk in found_ids ?
        return Movie.objects.filter(Q(title__icontains=search_term))





def persist_movie(imdb_id):
    movie_details = get_movie_details(imdb_id)
    log.warning(f"Fetched movie details: {movie_details}")

    return Movie.from_movie_details(movie_details)


class WatchedMoviesListView(ListView):
    model = Movie
    template_name = "movies/movies.html"
    context_object_name = "movies"

    def get_queryset(self):
        return Movie.objects.filter(Q(watched_by=self.request.user))


class NowPlayingMoviesListView(ListView):
    model = Movie
    template_name = "movies/movies.html"
    context_object_name = "movies"

    def get_queryset(self):
        imdb_ids = list(get_now_playing_imdb_ids())
        log.warning(f"\n\n/!\\ List of now playing movies: {imdb_ids}")

        new_movie_imdb_ids = [imdb_id for imdb_id in imdb_ids if not Movie.objects.filter(Q(pk=imdb_id)).exists()]
        log.warning(f"\n\n/!\\ List of new movies: {new_movie_imdb_ids}")

        for id in new_movie_imdb_ids:
            movie_details = get_movie_details(id)
            Movie.from_movie_details(movie_details)

        matches = Movie.objects.filter(Q(pk__in=imdb_ids))
        return matches

# class LatestMoviesListView(ListView):
#     model = Movie
#     template_name = "movies/movies.html"
#     context_object_name = "movies"

#     def get_queryset(self):
#         return Movie.objects.filter(Q(pk in [x.pk for x in LatestMovie.objects.all]))
