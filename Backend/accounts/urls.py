# accounts/urls.py
from django.urls import path
from .views import LoginView, ProfileView, CreateUserView, UserListView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('create/', CreateUserView.as_view()),
    path('users/', UserListView.as_view()),
]
