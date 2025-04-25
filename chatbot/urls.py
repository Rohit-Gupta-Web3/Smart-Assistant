from django.urls import path
from . import views, api_views

urlpatterns = [
    path("", views.chat_view, name="chat"),  # Render chat.html
    path("api/chat/", api_views.ChatAPIView.as_view(), name="api_chat"),  # API endpoint
]
