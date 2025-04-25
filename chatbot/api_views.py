from rest_framework.views import APIView
from rest_framework.response import Response
from transformers_model.model import generate_response
from .memory import get_or_create_session, build_prompt, save_message

class ChatAPIView(APIView):
    def post(self, request):
        user_msg = request.data.get("message", "")
        session_id = request.session.get("chat_session_id")

        session = get_or_create_session(session_id)
        request.session["chat_session_id"] = str(session.id)

        save_message(session, user_msg, is_user=True)
        prompt = build_prompt(session)
        bot_reply = generate_response(prompt)

        save_message(session, bot_reply, is_user=False)
        return Response({"response": bot_reply})
