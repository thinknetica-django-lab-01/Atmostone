from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse
from django.views.generic import UpdateView
from django.contrib.auth.models import User

from apps.profile.forms import ProfileForm


class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'profile/profile_update.html'
    login_url = 'login/'
    success_url = '/'

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        form.save(commit=False)
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

