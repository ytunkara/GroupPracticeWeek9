# users/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'), # Maps the URL /login/ to the login view
    #path('feedback/', views.feedback, name='feedback'),
]