from django import forms
# for user creation
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from .models import User


class SpForm(forms.Form):
    formsDotPyTextField = forms.CharField(label='Enter your text')


# This class was copied from
# https://ordinarycoders.com/django-user-registration
class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
