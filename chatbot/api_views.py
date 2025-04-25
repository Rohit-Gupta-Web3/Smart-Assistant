from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Session, Message
from .memory import MemoryHandler
from transformers_model.model import ModelProcessor


class ChatAPIView(APIView):
    def post(self, request):
        message = request.data.get("message")
        user_id = request.data.get("user_id")

        # Memory handler to check session
        session = MemoryHandler.get_or_create_session(user_id)

        # AI model processing
        response = ModelProcessor.generate_response(message)

        # Store message and session memory
        Message.objects.create(session=session, sender="user", message=message)
        Message.objects.create(session=session, sender="bot", message=response)
        session.memory = MemoryHandler.update_memory(session.memory, message, response)
        session.save()

        return Response({"response": response}, status=status.HTTP_200_OK)
