from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

class SignUpForm(UserCreationForm):
    username = forms.CharField(label = "", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(label = "", widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(label = "", widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), )
    password2 = forms.CharField(label = "", widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder':'username'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder':'password'}))
