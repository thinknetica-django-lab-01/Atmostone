from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import UpdateView
from django.contrib.auth.models import User

from apps.profile.forms import UserForm, ProfileForm
from apps.profile.models import Profile


class UserUpdate(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'profile/form.html'
    login_url = 'login/'
    success_url = '/'

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        form.save(commit=False)
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profile/form.html'
    login_url = 'login/'
    success_url = '/'

    def get_object(self):
        return Profile.objects.filter(user=self.request.user).first()

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
