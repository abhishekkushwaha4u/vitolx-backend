from django.urls import path
from chat import views

urlpatterns = [
    path('sendMessage/', views.MessageCreateView.as_view()),
    path('updateChat/', views.GetUnreadChatView.as_view()),
]