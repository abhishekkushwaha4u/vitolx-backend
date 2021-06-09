from django.urls import path
from exchange import views

urlpatterns = [
    path('addExchange/', views.ProductExchangeView.as_view()),
]