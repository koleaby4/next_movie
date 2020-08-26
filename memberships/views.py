from project.settings import STRIPE_PUBLIC_KEY

# Create your views here.

from django.views.generic.base import TemplateView

class MembershipsPageView(TemplateView):
    template_name = "memberships/purchase.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["stripe_key"] = STRIPE_PUBLIC_KEY
        return context
