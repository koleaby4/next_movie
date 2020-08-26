from django.urls import path

from .views import MovieDetailView, MovieListView, about

urlpatterns = [
    path("", MovieListView.as_view(), name="movie_list"),
    path("<slug:pk>", MovieDetailView.as_view(), name="movie_detail"),
    path("about", about, name="about"),
]
