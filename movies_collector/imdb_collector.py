import concurrent.futures
import json
import logging
import re
from pathlib import Path
from typing import Dict, List, Union
from urllib.parse import quote

import requests
from utils.utilities import get_secret

log = logging.getLogger(__name__)

RAPID_API_IMDB8_KEY = get_secret("RAPID_API_IMDB8_KEY")
OMDB_API_KEY = get_secret("OMDB_API_KEY")
TMDB_API_KEY = get_secret("TMDB_API_KEY")

def get_top_rated_movies():
    """Generator which yields most popular movies of all times"""

    # headers = {"x-rapidapi-host": "imdb8.p.rapidapi.com", "x-rapidapi-key": RAPID_API_IMDB8_KEY}
    # url = "https://imdb8.p.rapidapi.com/title/get-top-rated-movies"
    # response = requests.request("GET", url, headers=headers)
    # records = json.loads(response.text)

    # temporary stub. ToDo: replace when going live
    content = (Path(__file__).parent / "top_rated_movies_subset.json").read_text()
    records = json.loads(content)

    for entry in records:
        imdb_id = re.search(r"/title/(tt[0-9]+)/", entry["id"]).group(1)
        yield imdb_id

def get_movie_details(imdb_id: str) -> Dict:
    """Return movie details for movie with imdb_id"""
    movie_by_imdb_id_url = f"http://www.omdbapi.com/?i={imdb_id}&apikey={OMDB_API_KEY}"

    result = requests.get(movie_by_imdb_id_url).json()
    result["images"] = get_movie_images(imdb_id)

    log.warning(f"\n\nFetched movie details from omdbapi: {result}")
    return result

def search_movies(search_term: str) -> List[Dict]:
    """Return list of movies which contain <search_term> in title of plot"""

    encoded_term = quote(search_term)
    url = f"http://www.omdbapi.com/?s={encoded_term}&apikey={OMDB_API_KEY}"

    response_json = requests.get(url).json()
    if response_json.get("Response") == "False":
        return []

    return response_json.get("Search")

def url_exists(url: str) -> bool:
    """Return True if `url` exists and False otherwise"""
    try:
        return requests.get(url).status_code == 200
    except Exception:
        return False

def get_movie_reviews(imdb_id: str, count=5) -> List[Dict]:
    """Return top `count` reviews for movies with `imdb_id`"""

    url = "https://imdb8.p.rapidapi.com/title/get-user-reviews"

    querystring = {"tconst":imdb_id}

    headers = {
        'x-rapidapi-host': "imdb8.p.rapidapi.com",
        'x-rapidapi-key': RAPID_API_IMDB8_KEY
        }

    log.warning(f"\n\nFetching reviews for movie: {imdb_id}")
    response = requests.request("GET", url, headers=headers, params=querystring).json()

    reviews_count = response.get("totalReviews")
    log.warning(f"Number of reviews found: {reviews_count}")

    return response.get("reviews")[:count] if reviews_count else []


def get_now_playing_imdb_ids() -> List[str]:
    """Return list of imdb_ids of movies which are currently playing in cinemas """

    url = fr"https://api.themoviedb.org/3/movie/now_playing?api_key={TMDB_API_KEY}&language=en-GB&page=1"

    log.warning(f"\nFetching 'Now Playing' movies")

    response = requests.request("GET", url).json()
    tmdb_results = response["results"]

    log.warning(f"\n'Now Playing' movies: {tmdb_results}")

    imdb_ids = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        promises = []
        for entry in tmdb_results:
            promises.append(executor.submit(get_tmdb_movie_detail, tmdb_id=entry["id"]))

        for promise in concurrent.futures.as_completed(promises):
            tmdb_detail = promise.result()
            imdb_id = tmdb_detail.get("imdb_id")

            if imdb_id:
                imdb_ids.append(imdb_id)
            else:
                log.error(f"\n\nEmpty imdb_id field in TMDB database. Skipping this movie: {tmdb_detail}")

    return imdb_ids

def get_tmdb_movie_detail(tmdb_id: str) -> Union[Dict, List]:
    """Return movie details from api.themoviedb.org"""

    url = fr"https://api.themoviedb.org/3/movie/{tmdb_id}?api_key={TMDB_API_KEY}&language=en-GB"
    log.warning(f"\n\nFetching tmdb movie detail by id {tmdb_id}")

    result = requests.request("GET", url).json()
    log.warning(f"TMDB detail: {result}\n")

    return result


def get_movie_images(imdb_id: str) -> Dict:
    """Return collection of images for movie with imdb_id """

    url = "https://imdb8.p.rapidapi.com/title/get-images"

    querystring = { "limit" : "25", "tconst" : imdb_id }

    headers = {
        'x-rapidapi-host': "imdb8.p.rapidapi.com",
        'x-rapidapi-key': RAPID_API_IMDB8_KEY
        }

    return requests.request("GET", url, headers=headers, params=querystring).json()
