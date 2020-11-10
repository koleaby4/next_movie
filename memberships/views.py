import stripe
from django.contrib.auth.models import Permission
from django.shortcuts import render
from django.views.generic.base import TemplateView

from project.settings import STRIPE_PUBLISHABLE_KEY, STRIPE_SECRET_KEY


stripe.api_key = STRIPE_SECRET_KEY


class MembershipsPageView(TemplateView):
    template_name = "memberships/purchase.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["stripe_key"] = STRIPE_PUBLISHABLE_KEY
        return context


def charge(request):
    if request.method == "POST":
        stripe.Charge.create(
            amount=999,
            currency="gbp",
            description="Prime Membership",
            source=request.POST["stripeToken"],
        )

        paid_for_membership_permission = Permission.objects.get(codename="paid_for_membership")
        user = request.user
        user.user_permissions.add(paid_for_membership_permission)

        return render(request, "memberships/charge.html")
