from django.shortcuts import render, redirect, reverse
from django.views import View
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


from src.core.forms import LoginForm, RegisterForm
from src.hitmens.services import create_user

# Create your views here.
class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'core/login.html'
    success_url = reverse_lazy('core:home')


def logout_view(request):
    logout(request)
    return redirect(reverse("core:home"))


class Indexview(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request, *args, **kwargs):
        return render(request, 'core/index.html', locals())


class RegisterHitmenView(View):

    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, 'core/register.html', {'form':form})

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse("core:home"))

        form = RegisterForm(request.POST)
        if form.is_valid():
            create_user(form.cleaned_data)
            return redirect(reverse('core:home'))
        else:
            return render(request, 'core/register.html', {'form':form})