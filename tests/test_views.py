from rest_framework.test import APITestCase
from rest_framework import status
from chatbot.models import Session


class ChatAPIViewTest(APITestCase):
    def test_chat_view(self):
        Session.objects.create(user_id="test_user")
        response = self.client.post(
            "/api/chat/", {"message": "Hi", "user_id": "test_user"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
