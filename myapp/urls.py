from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('index/', views.indexView, name='index'),
    path('signup/', views.signupView, name='signup'),
    path('signin/', views.signinView, name='signin'),
    path('signout/', views.signoutView, name='signout'),
    path('delete/<int:num>', views.deleteView, name='delete'),
    path('', views.topView, name='top'),
]