from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class ProfileForm(forms.ModelForm):
    age = forms.IntegerField(min_value=0)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18:
            raise ValidationError("You must be 18 or older!")
        return age
