from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms
from django.forms.widgets import PasswordInput, TextInput


# -- register user
class CreateUserForm(UserCreationForm): 

    username = forms.CharField(
        label='Username',
        widget=TextInput(),
        error_messages={
            'unique': 'This username is already taken. Please choose a different one.',
        }
    )
    password1 = forms.CharField(
        label='Password',
        widget=PasswordInput(),
        error_messages={
            'password_mismatch': 'The two password fields didn’t match.',
        }
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=PasswordInput(),
    )


    class Meta:

        model = User
        fields = ["username", "password1", "password2"]

#-- login user
class LoginUserForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())