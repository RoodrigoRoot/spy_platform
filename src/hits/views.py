from typing import Dict, Any

from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError

from src.hits.selectors import get_all_my_hits
from src.hits.models import Hit
from src.hits.forms import FormStatusHit
from src.hits.transitions.hit import transition
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
        context['form'] = FormStatusHit()
        return context

    def post(self, request, *args, **kargs):
        object: Hit = self.get_object()
        form = FormStatusHit(request.POST)
        print(request.user.hitmen == object.assigned)
        if form.is_valid():
            try:
                transition(object, form.cleaned_data['status'])
                return render( request, self.template_name, locals())
            except ValidationError as e:
                message_error = ''.join(e)
                return render( request, self.template_name, locals())
            except Exception as e:
                message_error = str(e)
                return render( request, self.template_name, locals())
        else:
            print(form.errors)
            return render( request, self.template_name, locals())

