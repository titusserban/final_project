from django import forms

from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('avatar',)
        # "," din tuplu permite sa generam un formular cu un field care permite upload-ul de fisiere
