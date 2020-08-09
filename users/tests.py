from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class CreateUserTests(TestCase):
    def test_create_user(self):
        user = get_user_model().objects.create_user(
            username="James", email="james_007@mi6.co.uk", password="Str0ngP@ssword!"
        )

        self.assertEqual("james_007@mi6.co.uk", user.email)
        self.assertTrue(user.is_active)


class SignupTests(TestCase):
    def test_signup_page(self):
        signup_page_url = reverse("signup")
        response = self.client.get(signup_page_url)

        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, "signup.html")
        self.assertContains(response, "Sign up")
