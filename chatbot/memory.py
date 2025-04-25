from .models import Message, Session

def get_or_create_session(session_id=None):
    if session_id:
        session = Session.objects.filter(id=session_id).first()
        if session:
            return session
    return Session.objects.create()

def build_prompt(session):
    messages = Message.objects.filter(session=session).order_by("timestamp")
    prompt = ""
    for msg in messages:
        role = "User" if msg.is_user else "Bot"
        prompt += f"{role}: {msg.content}\n"
    return prompt.strip()

def save_message(session, content, is_user=True):
    return Message.objects.create(session=session, content=content, is_user=is_user)
