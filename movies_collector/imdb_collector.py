import os
import requests
import sys
import json

from pathlib import Path
project_root = str(Path(__file__).parents[1])
sys.path.append(project_root)

from utils.utilities import get_secret


headers = {
    'x-rapidapi-host': "imdb8.p.rapidapi.com",
    'x-rapidapi-key': get_secret("RAPID_API_IMDB8_KEY")
    }


def get_top_rated():
    # url = "https://imdb8.p.rapidapi.com/title/get-top-rated-movies"
    # response = requests.request("GET", url, headers=headers)
    # payload = json.loads(response.text)

    # temporary stub. ToDo: replace when going live
    content = (Path(__file__).parent / 'movies_rapid_api_STUB.json').read_text()
    payload = json.loads(content)

    return payload
