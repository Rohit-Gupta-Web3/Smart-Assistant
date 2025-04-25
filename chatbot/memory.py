from .models import Session


class MemoryHandler:
    @staticmethod
    def get_or_create_session(user_id):
        session, created = Session.objects.get_or_create(user_id=user_id)
        return session

    @staticmethod
    def update_memory(memory, user_message, bot_response):
        memory["history"].append({"user": user_message, "bot": bot_response})
        return memory
