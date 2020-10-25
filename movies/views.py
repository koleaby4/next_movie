import logging
import threading
from random import choice
from typing import List

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect, render, reverse
from django.views.generic import DetailView, ListView
from movies_collector.imdb_collector import (
    get_now_playing_imdb_ids,
    get_top_rated_movies,
    search_movies,
)

from movies.models import Movie

log = logging.getLogger(__name__)


class BestEverMovieListView(ListView):
    model = Movie
    template_name = "movies/movies.html"
    context_object_name = "movies"

    def get_queryset(self):
        return _best_unwatched_movies(self.request)[:22]


def _best_unwatched_movies(request):
    watched_movie_ids = []

    if request.user.is_authenticated:
        watched_movie_ids = [x.imdb_id for x in request.user.profile.watched_movies.all()]

    top_rated_movie_ids = tuple(get_top_rated_movies())

    for imdb_id in top_rated_movie_ids:
        if not Movie.objects.filter(pk=imdb_id).exists():
            Movie.persist_movie(imdb_id)

    q = Movie.objects.filter(imdb_id__in=top_rated_movie_ids)
    q = q.exclude(imdb_id__in=watched_movie_ids)
    q = q.order_by("-imdb_rating")

    return q.all()


class MovieDetailView(LoginRequiredMixin, DetailView):
    model = Movie
    template_name = "movies/movie_detail.html"
    context_object_name = "movie"
    login_url = "account_login"
    permission_required = "movies.paid_for_membership"

    @staticmethod
    def toggle_watched(request, pk):
        movie = Movie.objects.get(pk=pk)

        profile = request.user.profile

        log.warn(f"\nWatched movies before: {profile.watched_movies.all()}")

        if profile.watched_movies.filter(pk=movie.pk).exists():
            log.warn(f"\nRemoving movie ({movie}) from profile ({profile})")
            profile.watched_movies.remove(movie)
        else:
            log.warn(f"\nAdding movie ({movie}) to profile ({profile})")
            profile.watched_movies.add(movie)

        log.warn(f"\nWatched movies after: {profile.watched_movies.all()}")

        profile.save()

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

        return Movie.objects.filter(Q(imdb_id__in=found_ids))


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
        return _playing_now_movies()


def _playing_now_movies() -> List[Movie]:
    movies = []
    for imdb_id in get_now_playing_imdb_ids():
        try:
            movie = Movie.objects.get(pk=imdb_id)
        except Movie.DoesNotExist:
            movie = Movie.persist_movie(imdb_id)
        movies.append(movie)

    return movies


def index(request):

    context = {
        "next_best_movie": choice(_best_unwatched_movies(request)[:10]),
        "playing_now_movie": choice(_playing_now_movies()),
    }

    return render(request, "index.html", context=context)
