from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login),
    path('signup/',views.signUp),
    path('users/',views.getUsers)
]