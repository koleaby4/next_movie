from django.urls import path
from .views import MembershipsPageView


urlpatterns = [
    path("", MembershipsPageView.as_view(), name="memberships")
]
