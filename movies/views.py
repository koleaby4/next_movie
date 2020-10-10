import json
import logging
import re
import sys
from pathlib import Path
import threading
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect, render, reverse
from django.views.generic import DetailView, ListView

from movies.models import Movie, Review
from movies_collector.imdb_collector import (get_now_playing_imdb_ids,
                                             get_top_rated_movies,
                                             search_movies)

log = logging.getLogger(__name__)


class BestEverMovieListView(ListView):
    model = Movie
    template_name = "movies/movies.html"
    context_object_name = "movies"

    def get_queryset(self):
        results = []

        for imdb_id in get_top_rated_movies():
            if not Movie.objects.filter(pk=imdb_id).exists():
                movie = Movie.persist_movie(imdb_id)
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
        profile = user.profile

        if profile.watched_movies.filter(pk = movie.pk).exists():
            log.warn(f"\nRemoving movie ({movie}) from profile ({profile})")
            profile.watched_movies.remove(movie)
        else:
            log.warn(f"\nAdding movie ({movie}) to profile ({profile})")
            profile.watched_movies.add(movie)

        profile.save()
        # movie.save()

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

        threads = []
        for imdb_id in found_ids:
            if not Movie.objects.filter(pk=imdb_id).exists():
                t = threading.Thread(target=Movie.persist_movie, args=(imdb_id,))
                t.start()
                threads.append(t)

        for t in threads:
            t.join()

        # ToDo: change to pk in found_ids ?
        return Movie.objects.filter(Q(title__icontains=search_term))


class WatchedMoviesListView(ListView):
    model = Movie
    template_name = "movies/movies.html"
    context_object_name = "movies"

    def get_queryset(self):
        return Movie.objects.filter(Q(profile=self.request.user.profile))


class NowPlayingMoviesListView(ListView):
    model = Movie
    template_name = "movies/movies.html"
    context_object_name = "movies"

    def get_queryset(self):
        movies = []
        for imdb_id in get_now_playing_imdb_ids():
            try:
                movie = Movie.objects.get(pk=imdb_id)
            except Movie.DoesNotExist:
                movie = Movie.persist_movie(imdb_id)
            movies.append(movie)

        return movies

def index(request):
    return render(request, "index.html")
