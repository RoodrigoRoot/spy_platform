from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView
from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin

from src.hitmens.models import Hitmen

# Create your views here.

class HitmenListView(LoginRequiredMixin, AccessMixin, ListView):
    model = Hitmen

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            # This will redirect to the login view
            return self.handle_no_permission()
        if not self.request.user.groups.filter(name__in=['BigBoss', 'Manager']).exists():
            # Redirect the user to somewhere else - add your URL here
            return redirect(reverse("hits:hits"))

        # Checks pass, let http method handlers process the request
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Hitmen.objects.get_subordinates_all(self.request.user.email)