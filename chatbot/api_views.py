from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Message, Session
from transformers_model.model import (
    generate_response,
)  # Adjust import based on your project structure


class ChatAPIView(APIView):
    def post(self, request):
        user_msg = request.data.get("message", "")
        session_id = request.session.get("chat_session_id")

        session = get_or_create_session(session_id)
        request.session["chat_session_id"] = str(session.id)

        save_message(session, user_msg, is_user=True)
        prompt = build_prompt(session)
        bot_reply = generate_response(prompt, max_tokens=1000)

        save_message(session, bot_reply, is_user=False)
        return Response({"response": bot_reply})


def get_or_create_session(session_id=None):
    if session_id:
        session = Session.objects.filter(id=session_id).first()
        if session:
            return session
    return Session.objects.create()


def build_prompt(session):
    messages = Message.objects.filter(session=session).order_by("created_at")
    prompt = ""
    for msg in messages:
        role = "User" if msg.sender == "user" else "Bot"
        prompt += f"{role}: {msg.message}\n"
    return prompt.strip()


def save_message(session, content, is_user=True):
    sender = "user" if is_user else "bot"
    return Message.objects.create(session=session, sender=sender, message=content)
