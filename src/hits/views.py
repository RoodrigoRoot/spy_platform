from typing import Dict, Any

from django.shortcuts import render, redirect, reverse
from django.views import View
from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.core.exceptions import ValidationError

from src.hits.selectors import get_all_my_hits
from src.hits.models import Hit
from src.hits.forms import FormStatusHitmen, FormAssignedHit, CreateHitFormModel
from src.hits.transitions.hit import transition
from src.hitmens.models import Hitmen
from src.hits.services import update_assigned_hit, create_hit

# Create your views here.

class HitsView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request, *args, **kwargs):
        hits = get_all_my_hits(request.user.email)
        return render(request, 'hits/hits.html', locals())


class HitDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Hit
    template_name = 'hits/hit_detail.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(HitDetailView, self).get_context_data(**kwargs)
        context['form'] = FormStatusHitmen()
        context['form_assigned'] = FormAssignedHit()
        context['subordinates'] = Hitmen.objects.get_subordinates_all(self.request.user.email)
        return context

    def post(self, request, *args, **kargs):
        object: Hit = self.get_object()
        form = FormStatusHitmen(request.POST)
        form_assigned = FormAssignedHit(request.POST)
        if request.POST.get('status_hitmen', False):
            if form.is_valid():
                try:
                    transition(object, form.cleaned_data['status_hitmen'])
                    message = 'Status hitmen updated'
                    return render( request, self.template_name, locals())
                except ValidationError as e:
                    message_error = ''.join(e)
                    return render( request, self.template_name, locals())
                except Exception as e:
                    message_error = str(e)
                    return render( request, self.template_name, locals())
            else:
                return render( request, self.template_name, locals())

        else:
            if form_assigned.is_valid():
                try:
                    update_assigned_hit(object.pk, form_assigned.cleaned_data.get('assigned'))
                    message_assigned = 'Hitmen updated'
                    return render( request, self.template_name, locals())
                except ValidationError as ve:
                    message_assigned_error = ''.join(ve)
                    return render( request, self.template_name, locals())
            else:
                return render( request, self.template_name, locals())


class HitCreateView(LoginRequiredMixin,AccessMixin, CreateView):
    model = Hit
    form_class = CreateHitFormModel
    success_url = "/hits/"
    template_name = 'hits/hit_create.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            # This will redirect to the login view
            return self.handle_no_permission()
        if not self.request.user.groups.filter(name__in=['BigBoss', 'Manager']).exists():
            # Redirect the user to somewhere else - add your URL here
            return redirect(reverse("hits:hits"))

        # Checks pass, let http method handlers process the request
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(email=request.user.email)
        return render(request, self.template_name, locals())

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, email=request.user.email)
        if form.is_valid():
            create_hit(form.cleaned_data, request.user.hitmen)
        return render(request, self.template_name, locals())
