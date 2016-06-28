from django.shortcuts import render, redirect
from django.contrib.auth import (
    authenticate, 
    get_user_model,
    login,
    logout,
                                 )
from account.forms import UserLoginForm
# Create your views here.
def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        profil = {
                  "username": request.user.get_full_name(),
                  }
        if request.user.is_authenticated():
           return redirect('index') 
    return render(request, "login.html", {})

def index(request):
    return render(request, "index.html", {})

def logout_view(request):
    logout(request)
    return render(request, "login.html", {})