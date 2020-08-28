from django.urls import path

from .views import MovieDetailView, MovieListView, SearchResultsListView

urlpatterns = [
    path("", MovieListView.as_view(), name="movie_list"),
    path("<slug:pk>", MovieDetailView.as_view(), name="movie_detail"),
    path("search/", SearchResultsListView.as_view(), name="search_results"),
]
