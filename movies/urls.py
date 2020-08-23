from django.urls import path
from .views import index, about, MovieListView

urlpatterns = [
    path('', MovieListView.as_view(), name="movie_list"),
    path('about/', about, name="about"),
]
