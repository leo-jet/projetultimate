from django.shortcuts import render
from sympy import *
import random
from django.db import models
from monbord.modules.complexes import *
from django.core.files import File
import os
import json 

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#latex
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from subprocess import Popen, PIPE
import tempfile


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

def complexes(request):
    content = []
    return render(request, "complexes.html", content)

def logout_view(request):
    logout(request)
    return render(request, "login.html", {})

def chatroom(request):
    return render(request, "room.html", {})