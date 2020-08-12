import json
import os
import sys
from pathlib import Path

import requests

from utils.utilities import get_secret

RAPID_API_IMDB8_KEY = get_secret("RAPID_API_IMDB8_KEY")


def get_top_rated():

    # headers = {"x-rapidapi-host": "imdb8.p.rapidapi.com", "x-rapidapi-key": RAPID_API_IMDB8_KEY}
    # url = "https://imdb8.p.rapidapi.com/title/get-top-rated-movies"
    # response = requests.request("GET", url, headers=headers)
    # payload = json.loads(response.text)

    # temporary stub. ToDo: replace when going live
    content = (Path(__file__).parent / "movies_rapid_api_STUB.json").read_text()
    payload = json.loads(content)

    return payload


def get_movie_details(movie_id):
    url = f"https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/{movie_id}"

    headers = {
        "x-rapidapi-host": "imdb-internet-movie-database-unofficial.p.rapidapi.com",
        "x-rapidapi-key": RAPID_API_IMDB8_KEY,
    }

    response = requests.request("GET", url, headers=headers)
    return json.loads(response.text)
