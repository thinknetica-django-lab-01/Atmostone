from django import forms
from django.contrib.auth.models import User

from apps.profile.models import Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone', 'sex', 'date_of_birth',
                  'home_address', 'subscription')
