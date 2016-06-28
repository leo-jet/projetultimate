from django.shortcuts import render

# Create your views here.
from django.contrib.auth import (
    authenticate, 
    get_user_model,
    login,
    logout,
                                 )
from .forms import UserLoginForm

def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        print(request.user.is_authenticated())
    return render(request, "index.html", {})
    
def logout_view(request):  
    return render(request, "index.html", {})