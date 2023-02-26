from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class MyUserCreationForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'id': 'floatingInput1',
        'placeholder': 'name'
    }))

    email = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'email',
        'class': 'form-control',
        'id': 'floatingInput2',
        'placeholder': 'name@example.com'
    }))

    password1 = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'password',
        'class': 'form-control',
        'id': 'floatingPassword1',
        'placeholder': 'Password',
        'autofocus': "autofocus"
    }))

    password2 = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'password',
        'class': 'form-control',
        'id': 'floatingPassword2',
        'placeholder': 'Confirm password'
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserAuthenticationForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'id': 'floatingInput',
        'placeholder': 'name',
        'autofocus': "autofocus"
    }))

    password = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'password',
        'class': 'form-control',
        'id': 'floatingPassword',
        'placeholder': 'name@example.com'
    }))

    class Meta:
        model = User
        fields = ['username', 'password']
