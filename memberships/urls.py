from django.urls import path

from .views import MembershipsPageView, charge

urlpatterns = [
    path("", MembershipsPageView.as_view(), name="memberships"),
    path("charge/", charge, name="charge"),
]
