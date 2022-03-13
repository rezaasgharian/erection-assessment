from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

# Create your tests here.
from questionnaire.models import Questionnaire


# class QuestionnaireTestCase(APITestCase):
#
#     def authenticate(self):
#         self.client.post(reverse('register'), {
#             'username': 'username',
#             'email': 'username@gmail.com',
#             'password': 'username',
#             'password_confirmation': 'username',
#             'first_name': 'first_name',
#             'last_name': 'last_name'
#
#         })
#         response = self.client.post(reverse('login'), {
#             'username': 'username',
#             'password': 'username'
#         })
#         self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {response['access']}")
#         self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
#
#     def test_questionnaire_should_not_create_with_no_auth(self):
#         data = {
#             'user': '1',
#             'confidence': '3',
#             'penetration': '4',
#             'intercourse': '5',
#             'completion': '4',
#             'satisfaction': '4',
#         }
#         response = self.client.post(reverse('add_questionnaire'), data)
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
#
#     def test_questionnaire_should_create(self):
#         self.authenticate()
#         previous_questionnaire_count = Questionnaire.objects.all().count()
#         data = {
#             'user': '1',
#             'confidence': '3',
#             'penetration': '4',
#             'intercourse': '5',
#             'completion': '4',
#             'satisfaction': '4',
#         }
#         response = self.client.post(reverse('add_questionnaire'), data)
#         self.assertEqual(Questionnaire.objects.all().count(), previous_questionnaire_count + 1)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#
#     def test_retrieves_all_questionnaires(self):
#         self.authenticate()
#         response = self.client.get(reverse('questionnaires'))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertIsInstance(response.data['result'], list)
