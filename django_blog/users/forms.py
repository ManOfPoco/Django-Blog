from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Profile


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


class ProfileUpdateForm(forms.ModelForm):

    city = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'id': 'location',
        'placeholder': 'Enter your location',
    }), required=False)

    about = forms.CharField(widget=forms.Textarea(attrs={
        'type': 'text',
        'class': 'form-control autosize',
        'id': 'bio',
        'placeholder': 'Write something about you',
        "style": "overflow: hidden; overflow-wrap: break-word; resize: none; height: 62px;"
    }), required=False)

    image = forms.ImageField(required=False)

    class Meta:
        model = Profile
        fields = ['city', 'about', 'image']


class UserUpdateForm(forms.ModelForm):

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'id': 'fullName',
        'placeholder': 'Enter your first name',
        'aria-describedby': "NameHelp",
    }), required=False)

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'id': 'fullName',
        'placeholder': "Enter your last name",
        'aria-describedby': "LastNameHelp",
    }), required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name']
