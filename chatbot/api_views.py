from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .memory import get_context_memory, update_memory
from transformers_model.model import get_model_response

class ChatAPIView(APIView):
    def post(self, request):
        user_message = request.data.get("message", "")
        session_id = request.data.get("session_id", "default")

        context = get_context_memory(session_id)
        response_text = get_model_response(user_message, context)

        update_memory(session_id, user_message, response_text)

        return Response({"response": response_text}, status=status.HTTP_200_OK)
