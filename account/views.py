from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .form import RegisterUser, UserLogin
from django.contrib import messages


def register_view(request):
    regist = RegisterUser(request.POST or None)
    if User.objects.filter(username=request.POST.get("username")).exists():
        messages.error(request, "User with that name already exists")
    if request.POST.get("password") != request.POST.get("repeat_password"):
        messages.error(request, "Password do not match")
    if regist.is_valid():
        new_user = regist.save(commit=False)
        new_user.set_password(regist.cleaned_data["password"])
        new_user.save()
        login(request, new_user)
        return redirect("/")
    return render(request,"register.html",context={"regist":regist})

def login_view(request):
    form_login= UserLogin(request.POST or None)
    next_get = request.GET.get("next")
    if form_login.is_valid():
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, "Invalid password or username")
        else:
            login(request, user)
            next_post = request.POST.get("next")
            return redirect(next_get or next_post or "/")
    return render(request, "login.html", context={"form": form_login})

def logout_view(request):
    logout(request)
    return redirect("/")