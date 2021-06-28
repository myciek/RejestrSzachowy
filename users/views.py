from django.contrib.auth import login
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect

from users.forms import RegisterForm


def index(request):
    return render(request, "users/index.html")


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user = form.save()

            login(request, user)
            return redirect('index')
        else:
            form = RegisterForm()

    return render(request, "registration/register.html", {"form": form})
