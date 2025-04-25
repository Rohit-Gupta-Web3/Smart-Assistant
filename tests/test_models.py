from django.test import TestCase
from chatbot.models import Session, Message


class SessionModelTest(TestCase):
    def test_session_creation(self):
        session = Session.objects.create(user_id="test_user")
        self.assertEqual(session.user_id, "test_user")

    def test_message_creation(self):
        session = Session.objects.create(user_id="test_user")
        message = Message.objects.create(
            session=session, sender="user", message="Hello"
        )
        self.assertEqual(message.message, "Hello")
