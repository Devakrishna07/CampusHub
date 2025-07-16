from django.urls import path
from .views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register_user"),
    path("token/", TokenObtainPairView.as_view(), name="Token_obtain/login"),
    path("refresh_token/", TokenRefreshView.as_view(), name="Token_refresh")
]
