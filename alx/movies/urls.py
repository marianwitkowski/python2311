
from django.contrib import admin
from django.urls import path, include
from .views import *

from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", startpage_response ),
    path("list", movielist_response, name="movie_list" ),
    path("movieadd", movieadd_response),

    path("login", auth_views.LoginView.as_view() ),
    path("logout", auth_views.LogoutView.as_view(), name="logout" ),
    path("logout-done", logout_done)
]
