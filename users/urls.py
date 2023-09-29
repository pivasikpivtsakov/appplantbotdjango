from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from users import views

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("signup/", views.RegisterView.as_view()),
    path("profile/", views.UserProfileView.as_view()),
    path("usertoken/", views.CreateTelegramTokenView.as_view()),
]
