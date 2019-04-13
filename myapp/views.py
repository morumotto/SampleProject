from django.shortcuts import render, reverse
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import CustomUser
from .forms import CustomUserForm, LoginForm
from django.contrib.auth.views import LoginView, LogoutView
# Create your views here.


def topView(request):
    return render(request, "myapp/top.html")


def indexView(request):
    return render(request, "myapp/index.html")


class SignupView(CreateView):
    model = CustomUser
    form_class = CustomUserForm
    template_name = 'myapp/signup.html'
    success_url = reverse_lazy('myapp:index')
signupView = SignupView.as_view()


class SigninView(LoginView):
    form_class = LoginForm
    template_name = 'myapp/signin.html'
signinView = SigninView.as_view()