from django.shortcuts import render, reverse, redirect
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import CustomUser, Todo
from .forms import CustomUserForm, LoginForm, CreateTodoForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
# Create your views here.


def topView(request):
    return render(request, "myapp/top.html")


@login_required
def indexView(request):
    params = {
        'form': CreateTodoForm(),
        'todo': Todo.objects.filter(owner=request.user)
    }

    if request.method == "POST":
        todo = Todo(owner=request.user,
                    title=request.POST['title'],
                    contents=request.POST['contents'],
        )
        todo.save()
        return redirect('myapp:index')

    return render(request, 'myapp/index.html', params)


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


class SignoutView(LogoutView):
    pass
signoutView = login_required(SignoutView.as_view())


@login_required
def deleteView(request, num):
    Todo.objects.filter(pk=num).delete()
    return redirect('myapp:index')