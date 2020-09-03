from .forms import SignUpForm, LoginForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

def signup_form(request):
    form = SignUpForm()
    return {'formSignup': form}

def login_form(request):
    form = LoginForm()
    return {'formLogin': form}
