from django.urls import include, path
from .views import dashboard, profile_list, profile, register

app_name = "weconnect"

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("", dashboard, name="dashboard"),
    path("profile_list/", profile_list, name="profile_list"),
    path("profile/<int:pk>", profile, name="profile"),
    path("register/", register, name="register"),
]