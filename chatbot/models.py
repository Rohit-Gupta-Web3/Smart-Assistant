from django.db import models


class Session(models.Model):
    user_id = models.CharField(max_length=100, unique=True)
    memory = models.JSONField(default=dict)


class Message(models.Model):
    session = models.ForeignKey(
        Session, related_name="messages", on_delete=models.CASCADE
    )
    sender = models.CharField(max_length=10)  # 'user' or 'bot'
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
