from django.urls import path
from user import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('create/', views.CreateUserView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('profile/create/', views.CreateUserProfileView.as_view()),
    path('profile/view/', views.DisplayUserFullProfileView.as_view()),
    path('profile/update/', views.UpdateUserView.as_view()),
    path('profile/picture/update/', views.UpdateUserProfilePictureView.as_view()),
    path('notification/set/', views.UserNotificationTokenResetView.as_view()),
]