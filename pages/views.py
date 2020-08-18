from pathlib import Path
import sys

from django.shortcuts import render, HttpResponse, render
from movies_collector.imdb_collector import get_top_rated


from utils.utilities import get_secret

def index(request):
    top_rated_movies = get_top_rated()
    context = {"movies" : top_rated_movies}
    return render(request, 'index.html', context=context)

def about(request):
    return render(request, 'about.html')

def validate_domain(request):
    return HttpResponse("ok")
