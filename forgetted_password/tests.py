from rest_framework.test import APITestCase
from rest_framework import status

class TestResetPassword(APITestCase):
    def test_reset_psw(self):
        data = {
            "email" : "arisantisoekamto23@gmail.com",
            "password": "resetpassword",
            "confirm_password": "resetpassword"
        }
        response = self.client.post("/api/sys-reset-psw/", data)
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
