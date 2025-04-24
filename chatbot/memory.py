# For now, use in-memory dict. Later, link with DB or cache like Redis
session_memory = {}

def get_context_memory(session_id):
    return session_memory.get(session_id, "")

def update_memory(session_id, user_msg, bot_reply):
    history = session_memory.get(session_id, "")
    updated = f"{history}\nUser: {user_msg}\nBot: {bot_reply}"
    session_memory[session_id] = updated[-2000:]  # limit context size
