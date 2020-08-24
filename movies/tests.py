from django.test import TestCase
from django.urls import reverse
from movies.models import Movie
import json


class PagesTests(TestCase):

    def test_content_of_index_page(self):
        url = reverse("movie_list")
        response = self.client.get(url)

        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, "movies/movie_list.html")


class ModelsTests(TestCase):

    def test_valid_Movie_fields(self):

        movie = Movie.objects.create(
            imdb_id = "test_1",
            title = "Test Title",
            year = 1900,
            plot = "Some description of the TEST plot",
            poster_url = "http://dummy-url.com",
            imdb_rating = 8.1,
            full_json_details = '{"imdb_id" : "test_1"}'
        )

        self.assertEqual("test_1", movie.imdb_id)
        self.assertEqual("Test Title", movie.title)
        self.assertEqual(1900, movie.year)
        self.assertEqual("Some description of the TEST plot", movie.plot)
        self.assertEqual("http://dummy-url.com", movie.poster_url)
        self.assertEqual('{"imdb_id" : "test_1"}', movie.full_json_details)
