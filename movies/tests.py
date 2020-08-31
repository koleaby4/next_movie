from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from movies.models import Movie, Review
import json


class PagesTests(TestCase):
    def test_content_of_movies_page(self):
        url = reverse("movie_list")
        response = self.client.get(url)

        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, "movies/movies.html")


class ModelsTests(TestCase):
    def test_valid_Movie_fields(self):

        movie = Movie.objects.create(
            imdb_id="test_1",
            title="Test Title",
            year=1900,
            plot="Some description of the TEST plot",
            poster_url="http://dummy-url.com",
            imdb_rating=8.1,
            full_json_details='{"imdb_id" : "test_1"}',
        )

        self.assertEqual("test_1", movie.imdb_id)
        self.assertEqual("Test Title", movie.title)
        self.assertEqual(1900, movie.year)
        self.assertEqual("Some description of the TEST plot", movie.plot)
        self.assertEqual("http://dummy-url.com", movie.poster_url)
        self.assertEqual('{"imdb_id" : "test_1"}', movie.full_json_details)


class ReviewTests(TestCase):
    def test_review_creation(self):
        movie = Movie.objects.create(
            imdb_id="test_1",
            title="Test Title",
            year=1900,
            plot="Some description of the TEST plot",
            poster_url="http://dummy-url.com",
            imdb_rating=8.1,
            full_json_details='{"imdb_id" : "test_1"}',
        )

        author = get_user_model().objects.create(
            username="test_user",
            email="test_user@email.com",
            password="Str0ngP@ssw0rd!"
        )

        review = Review.objects.create(movie=movie, review="This is a test review!", author=author)

        self.assertEqual("This is a test review!", review.review)
