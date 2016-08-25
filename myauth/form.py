from django import forms
from django.contrib.auth import get_user_model, authenticate


def user_exists(email):
    return bool(len(get_user_model().objects.filter(email=email)))


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def is_valid(self):
        return all(self.data) and user_exists(self.data['email'])

    def authenticate(self):
        return authenticate(email=self.data['email'], password=self.data['password'])


class RegistrationForm(forms.Form):
    email = forms.EmailField()
    password1 = forms.CharField(label='Password1', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password2', widget=forms.PasswordInput)

    def is_valid(self):
        return all(self.data) and self.data['password1'] == self.data['password2'] and not user_exists(self.data['email'])

    def registrate(self):
        return get_user_model().objects.create_user(email=self.data['email'], password=self.data['password1'])