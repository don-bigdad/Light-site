from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .form import RegisterUser
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
        return redirect("/")
    return render(request,"register.html",context={"regist":regist})

def login_view(request):
    pass
def logout_view(request):
    pass