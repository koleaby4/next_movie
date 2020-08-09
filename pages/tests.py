from django.test import TestCase

class PagesTests(TestCase):

    def setUp(self):
        self.response = self.client.get('')


    def test_implicit_index_response_200(self):
        self.assertEqual(200, self.response.status_code)

    def test_index_template_used(self):
        self.assertTemplateUsed(self.response, 'index.html')

    def test_index_page_contains_movie_id(self):
        self.assertContains(self.response, 'tt0111161')
