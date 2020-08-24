from django.urls import path
from .views import index, about, MovieListView, MovieDetailView

urlpatterns = [
    path('', MovieListView.as_view(), name="movie_list"),
    path('<slug:pk>', MovieDetailView.as_view(), name="movie_detail"),
    path('about', about, name="about"),
]
