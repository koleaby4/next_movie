from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import ProfileView

urlpatterns = [
    path("", ProfileView.as_view(), name="profile"),
]
