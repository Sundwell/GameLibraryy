from django.contrib.auth import login
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import FormView
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm


class RegisterView(FormView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class UserLoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'registration/login.html'
    success_url = '/'

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)


class CustomLogoutView(LogoutView):
    template_name = 'base.html'
    next_page = reverse_lazy('core:register')

