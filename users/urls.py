"""users URL Configuration

"""

from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

app_name = 'users'
LoginView.template_name = 'users/login.html'

urlpatterns = [
    
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register', views.register, name='register'),
    
]