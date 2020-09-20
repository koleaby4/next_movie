import json
import logging
import os
import re
import sys
from pathlib import Path
from typing import List
from urllib.parse import quote

import requests

from utils.utilities import get_secret

log = logging.getLogger(__name__)

RAPID_API_IMDB8_KEY = get_secret("RAPID_API_IMDB8_KEY")
OMDB_API_KEY = get_secret("OMDB_API_KEY")
TMDB_API_KEY = get_secret("TMDB_API_KEY")




def get_top_rated_movies():

    # headers = {"x-rapidapi-host": "imdb8.p.rapidapi.com", "x-rapidapi-key": RAPID_API_IMDB8_KEY}
    # url = "https://imdb8.p.rapidapi.com/title/get-top-rated-movies"
    # response = requests.request("GET", url, headers=headers)
    # records = json.loads(response.text)

    # temporary stub. ToDo: replace when going live
    content = (Path(__file__).parent / "top_rated_movies_subset.json").read_text()
    records = json.loads(content)

    for entry in records:
        yield re.search(r"/title/(tt[0-9]+)/", entry["id"]).group(1)


def get_movie_details(movie_id):
    movie_by_imdb_id_url = f"http://www.omdbapi.com/?i={movie_id}&apikey={OMDB_API_KEY}"
    result = requests.get(movie_by_imdb_id_url).json()
    log.warning(f"\n\nFetched movie details from omdbapi: {result}")
    return result


def search_movies(search_term: str) -> List[str]:
    encoded_term = quote(search_term)

    movie_by_search_url = f"http://www.omdbapi.com/?s={encoded_term}&apikey={OMDB_API_KEY}"
    response_json = requests.get(movie_by_search_url).json()
    if response_json.get("Response") == "False":
        return []

    return response_json.get("Search")

def url_exists(url):
    try:
        return requests.get(url).status_code == 200
    except Exception:
        return False


def get_movie_reviews(movie_id, count=5):
    url = "https://imdb8.p.rapidapi.com/title/get-user-reviews"

    headers = {
        'x-rapidapi-host': "imdb8.p.rapidapi.com",
        'x-rapidapi-key': RAPID_API_IMDB8_KEY
        }

    log.warning(f"\n\nFetching reviews for movie: {movie_id}")
    response = requests.request("GET", url, headers=headers, params={"tconst":movie_id}).json()

    number_of_reviews_found = response.get("totalReviews")
    log.warning(f"Number of reviews found: {number_of_reviews_found}")

    if number_of_reviews_found == 0:
        return []

    return response.get("reviews")[:count-1]


def get_now_playing_imdb_ids():
    url = fr"https://api.themoviedb.org/3/movie/now_playing?api_key={TMDB_API_KEY}&language=en-GB&page=1"

    log.warning(f"\nFetching 'Now Playing' movies")
    response = requests.request("GET", url).json()
    tmdb_results = response["results"]
    log.warning(f"\n'Now Playing' movies: {tmdb_results}")

    for entry in tmdb_results:
        tmdb_detail = get_tmdb_movie_detail(entry["id"])
        log.warning(f"TMDB detail: {tmdb_detail}")

        imdb_id = tmdb_detail["imdb_id"]
        if imdb_id:
            yield imdb_id
        else:
            log.error(f"\n\nEmpty imdb_id field in TMDB database. Skipping this movie: {tmdb_detail}")
            continue

def get_tmdb_movie_detail(tmdb_id):
    url = fr"https://api.themoviedb.org/3/movie/{tmdb_id}?api_key={TMDB_API_KEY}&language=en-GB"
    log.warning(f"\n\nFetching tmdb movie detail by id {tmdb_id}")
    return requests.request("GET", url).json()
