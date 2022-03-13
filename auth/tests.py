from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


# Create your tests here.

class AuthenticationTestCase(APITestCase):
    def test_register(self):
        data = {
            'username': 'saeed',
            'email': 'saeed@gmail.com',
            'password': 'username12345',
            'password_confirmation': 'username12345',
            'first_name': 'saeed',
            'last_name': 'nabati',
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        data = {
            'username': 'admin',
            'password': 'admin'
        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout(self):
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)