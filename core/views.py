from django.contrib.auth import login
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, CreateView

from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        # return HttpResponseRedirect(reverse("index"))
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class UserLoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return HttpResponseRedirect(reverse("index"))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
