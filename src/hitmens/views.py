from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin
from django.core.exceptions import ValidationError

from src.hitmens.models import Hitmen
from src.hitmens.services import change_active_user
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

class HitmenDetailsDetailView(DetailView):
    model = Hitmen
    template_name = 'hitmens/hitmen_details.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        obj = context['object']
        context['subordinates'] = Hitmen.objects.get_subordinates_all(obj.user.email)
        return context

    def post(self, request, *args, **kwargs):
        object = self.get_object()
        subordinates = Hitmen.objects.get_subordinates_all(object.user.email)
        user = Hitmen.objects.get(id=self.kwargs['pk']).user
        new_status = bool(request.POST.get('is_active', ''))
        try:
            change_active_user(user, request.user, new_status)
            new_status = 'Active' if new_status else 'Disabled'
            message = f"User updated. New status is: {new_status}"
            return render(request, self.template_name, locals())
        except ValidationError as ve:
            message_error = ''.join(ve)
            return render(request, self.template_name, locals())
        except Exception as e:
            message_error = str(e)
            return render(request, self.template_name, locals())
