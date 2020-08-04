from django.test import TestCase
from django.contrib.auth import get_user_model

class CreateUserTests(TestCase):

    def test_create_user(self):
        user = get_user_model().objects.create_user(
            username="James",
            email="james_007@mi6.co.uk",
            password="Str0ngP@ssword!"
        )

        self.assertEqual("james_007@mi6.co.uk", user.email)
        self.assertTrue(user.is_active)
