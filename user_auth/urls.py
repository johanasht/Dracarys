from django.urls import path
from .views import register, login_user, logout_user, login_flutter, logout_flutter

app_name = "user_auth"

urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
    path("login-flutter/", login_flutter, name="login_flutter"),
    path("logout-flutter/", logout_flutter, name="logout_flutter")
]