from django.urls import path
from .views import (SignUpView, PetalLoginView, PetalLogoutView,
                    ProfileView, ProfileUpdateView)

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", PetalLoginView.as_view(), name="login"),
    path("logout/", PetalLogoutView.as_view(), name="logout"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("profile/edit/", ProfileUpdateView.as_view(), name="profile_edit"),
]