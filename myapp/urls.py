from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('index', views.indexView, name='index'),
    path('signup', views.signupView, name='signup'),
    path('signin', views.signinView, name='signin'),
    path('', views.topView, name='top')
]