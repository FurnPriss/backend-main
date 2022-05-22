from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from passlib.hash import sha256_crypt

# Create your tests here.
class RegistrationTestCase(APITestCase):
    def test_registration(self):
        data = {
            "email": "akhfzz23@gmail.com", 
            "name":"arazor", 
            "username": "akhfzz", 
            "password": sha256_crypt.hash("passwordfake")
        }
        response = self.client.post("/api/sys-regis/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)