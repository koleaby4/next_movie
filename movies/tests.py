from django.test import TestCase
from django.urls import reverse


class PagesTests(TestCase):
    def test_content_of_index_page(self):
        url = reverse("index")
        response = self.client.get(url)

        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, "index.html")
        self.assertContains(response, "tt0111161")

    def test_content_of_about_page(self):
        url = reverse("about")
        response = self.client.get(url)

        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, "about.html")
        self.assertContains(response, "On about page")
