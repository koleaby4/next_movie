import concurrent.futures
import logging
from random import choice
from typing import List

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect, render, reverse
from django.views.generic import DetailView, ListView
from movies_collector.imdb_collector import (get_now_playing_imdb_ids,
                                             get_top_rated_imdb_ids,
                                             search_movies)

from movies.models import Movie

log = logging.getLogger(__name__)


class BestEverMovieListView(ListView):
    model = Movie
    template_name = "movies/movies.html"
    context_object_name = "movies"

    def get_queryset(self):
        return _best_unwatched_movies(self.request)


def _best_unwatched_movies(request):
    """Return best movies excluding the ones watched by the current user"""

    watched_movie_ids = tuple(x.imdb_id for x in request.user.profile.watched_movies.all()) if request.user.is_authenticated else tuple()

    log.warning(f"Identifying _best_unwatched_movies")
    top_rated_movie_ids = tuple(get_top_rated_imdb_ids())

    unwatched_top_rated_slice = tuple(id for id in top_rated_movie_ids if id not in watched_movie_ids)[:21]

    movie_ids_to_save = set(id for id in unwatched_top_rated_slice if not Movie.objects.filter(pk=id).exists())
    persist_movies(movie_ids_to_save)

    log.warning(f"Filtering watched movies")
    q = Movie.objects.filter(imdb_id__in=unwatched_top_rated_slice)
    q = q.order_by("-imdb_rating")

    log.warning(f"Finished filtering watched movies")
    return q.all()


class MovieDetailView(LoginRequiredMixin, DetailView):
    model = Movie
    template_name = "movies/movie_detail.html"
    context_object_name = "movie"
    login_url = "account_login"
    permission_required = "movies.paid_for_membership"

    @staticmethod
    def toggle_watched(request, pk):
        """Mark movie watched / unwatched"""
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

        movie_ids_to_save = [id for id in found_ids if not Movie.objects.filter(pk=id).exists()]
        persist_movies(movie_ids_to_save)

        return Movie.objects.filter(Q(imdb_id__in=found_ids))


def persist_movies(movie_ids):
    if not movie_ids:
        return

    log.warning(f"Movie IDs to persist: {', '.join(movie_ids)}")

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = []

        for imdb_id in movie_ids:
            futures.append(executor.submit(Movie.persist_movie, imdb_id))

        for future in concurrent.futures.as_completed(futures):
            try:
                movie = future.result()
            except Exception as exc:
                log.error(f"Unable to persist movie with imdb_id {imdb_id}. Error detail: {exc}")
            else:
                log.warning(f"Successfully saved movie {movie}")

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
    """Persist all movies which are currently playing in cinemas and return them"""
    movies = []

    for imdb_id in get_now_playing_imdb_ids():
        try:
            movie = Movie.objects.get(pk=imdb_id)
        except Movie.DoesNotExist:
            movie = Movie.persist_movie(imdb_id)
        finally:
            movies.append(movie)

    return movies


def indexView(request):
    """View for index.html"""
    context = {
        "next_best_movie": choice(_best_unwatched_movies(request)[:10]),
        "playing_now_movie": choice(_playing_now_movies()),
    }

    return render(request, "index.html", context=context)
