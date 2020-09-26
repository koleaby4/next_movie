from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView

from profiles.models import Profile

class ProfileView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = "profiles/profile.html"
    context_object_name = "profile"
    login_url = "account_login"
