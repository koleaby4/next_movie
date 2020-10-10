from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import MovieDetailView, BestEverMovieListView, SearchResultsListView, WatchedMoviesListView, NowPlayingMoviesListView

urlpatterns = [
    path("", BestEverMovieListView.as_view(), name="best_ever"),
    path("watched/", login_required(WatchedMoviesListView.as_view()), name="watched"),
    path("now_playing/", NowPlayingMoviesListView.as_view(), name="now_playing"),
    path("search/", SearchResultsListView.as_view(), name="search_results"),
    path("<slug:pk>", login_required(MovieDetailView.as_view()), name="movie_detail"),
    path("<slug:pk>/toggle_watched", login_required(MovieDetailView.toggle_watched), name="toggle_watched"),
]
