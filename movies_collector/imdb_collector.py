import json
import os
import sys
from pathlib import Path
from urllib.parse import quote
import requests
from typing import List

from utils.utilities import get_secret
import re

RAPID_API_IMDB8_KEY = get_secret("RAPID_API_IMDB8_KEY")
OMDB_API_KEY = get_secret("OMDB_API_KEY")


def get_top_rated_movies():

    # headers = {"x-rapidapi-host": "imdb8.p.rapidapi.com", "x-rapidapi-key": RAPID_API_IMDB8_KEY}
    # url = "https://imdb8.p.rapidapi.com/title/get-top-rated-movies"
    # response = requests.request("GET", url, headers=headers)
    # records = json.loads(response.text)

    # temporary stub. ToDo: replace when going live
    content = (Path(__file__).parent / "top_rated_movies_subset.json").read_text()
    records = json.loads(content)
    imdb_ids = [re.search(r"/title/(tt[0-9]+)/", entry["id"]).group(1) for entry in records]
    return imdb_ids


def get_movie_details(movie_id):
    movie_by_imdb_id_url = f"http://www.omdbapi.com/?i={movie_id}&apikey={OMDB_API_KEY}"
    response = requests.request("GET", movie_by_imdb_id_url)

    return json.loads(response.text)

def search_movies(search_term: str) -> List[str]:
    encoded_term = quote(search_term)

    movie_by_search_url = f"http://www.omdbapi.com/?s={encoded_term}&apikey={OMDB_API_KEY}"
    response = requests.request("GET", movie_by_search_url)

    response_json = json.loads(response.text)
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

    response = requests.request("GET", url, headers=headers, params={"tconst":movie_id})
    reviews = json.loads(response.text).get("reviews")
    return reviews[:count-1] if reviews else []
