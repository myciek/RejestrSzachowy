from django.urls import path

from users.views import index, register, login

urlpatterns = [
    path("index/", index, name="index"),
    path('register/', register, name='register'),
]