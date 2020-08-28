import json
import os
import sys
from pathlib import Path
from urllib.parse import quote
import requests
from typing import List

from utils.utilities import get_secret

RAPID_API_IMDB8_KEY = get_secret("RAPID_API_IMDB8_KEY")
OMDB_API_KEY = get_secret("OMDB_API_KEY")


def get_top_rated_movies():

    # headers = {"x-rapidapi-host": "imdb8.p.rapidapi.com", "x-rapidapi-key": RAPID_API_IMDB8_KEY}
    # url = "https://imdb8.p.rapidapi.com/title/get-top-rated-movies"
    # response = requests.request("GET", url, headers=headers)
    # payload = json.loads(response.text)

    # temporary stub. ToDo: replace when going live
    content = (Path(__file__).parent / "top_rated_movies.json").read_text()
    payload = json.loads(content)

    return payload


def get_movie_details(movie_id):
    # !!! scarce resource - only 500 calls per month !!!
    #
    # url = f"https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/{movie_id}"

    # headers = {
    #     "x-rapidapi-host": "imdb-internet-movie-database-unofficial.p.rapidapi.com",
    #     "x-rapidapi-key": RAPID_API_IMDB8_KEY,
    # }

    # response = requests.request("GET", url, headers=headers)
    # return json.loads(response.text)

    # --------------------------------------------------

    # potentially less details, but we have many more free calls to omdb API
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
