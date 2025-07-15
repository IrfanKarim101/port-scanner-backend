from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class UserModelTests(TestCase):

    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = get_user_model().objects.create_user(username=self.username, password=self.password)

    def test_user_creation(self):
        self.assertEqual(self.user.username, self.username)
        self.assertTrue(self.user.check_password(self.password))

class AuthenticationViewsTests(TestCase):

    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = get_user_model().objects.create_user(username=self.username, password=self.password)

    def test_login_view(self):
        response = self.client.post(reverse('login'), {'username': self.username, 'password': self.password})
        self.assertEqual(response.status_code, 200)

    def test_logout_view(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Redirect after logout

    def test_registration_view(self):
        response = self.client.post(reverse('register'), {'username': 'newuser', 'password': 'newpassword'})
        self.assertEqual(response.status_code, 201)  # Assuming registration returns 201 on success