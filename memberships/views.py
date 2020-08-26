# from django.shortcuts import render

# Create your views here.

from django.views.generic.base import TemplateView

class MembershipsPageView(TemplateView):
    template_name = "memberships/purchase.html"
