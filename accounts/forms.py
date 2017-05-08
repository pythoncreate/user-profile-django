from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.core import validators

from . import models


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = models.UserProfile
        fields = [
            'first_name',
            'last_name',
            'email',
            'date_birth',
            'bio',
            'image',
        ]


class EditProfileForm(forms.ModelForm):
    verify_email = forms.EmailField(label = "Please verify email address")
    bio = forms.CharField(widget=forms.Textarea, min_length=10)

    class Meta:
        model = models.UserProfile
        fields = [
            'first_name',
            'last_name',
            'email',
            'verify_email',
            'date_birth',
            'bio',
            'image',
        ]

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data['email']
        verify = cleaned_data['verify_email']
        if email != verify:
            raise forms.ValidationError(
                "You need to enter same email in both fields."
            )

    def  clean_birth_date(self):
        date_birth = self.cleaned_data['date_birth']
