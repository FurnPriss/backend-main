from rest_framework.test import APITestCase
from rest_framework import status

class TestRegister(APITestCase):
    def test_register(self):
        data = {
            "email": "arisantisoekamto@gmail.com",
            "name": "arisanti soekamto",
            "username": "shasha",
            "password": "mama"
        }
        response = self.client.post("/api/sys-regis/", data)
        # self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
