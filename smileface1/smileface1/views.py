# I have created this website.


import argparse
from email.policy import default
import os
from django.http import HttpResponse
from django.shortcuts import redirect, render
#from pyexpat.errors import messages
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login as dj_login, logout
from django.contrib.auth.models import User
from smile.models import Smile as smilingimagestable
from subprocess import call
import test as mosaci


def index(request):

    smileImages = smilingimagestable.objects.all()

    # return HttpResponse("Hello")
    return render(request, 'index.html', {'smileImages': smileImages})


def aboutus(request):
    return render(request, 'aboutus.html')


def contactus(request):

    return render(request, 'contactus.html')


def mission(request):
    return render(request, 'mission.html')


def login(request):
    print("here")

    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def reasontosmile(request):
    return render(request, 'reasontosmile.html')


def click(request):
    return render(request, 'click.html')


def handlesignup(request):
    if request.method == 'POST':

        # Get Parameters
        username = request.POST["username"]
        user=username.lower()
        print(user)
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Checks
        if password == password2:
            if len(password) >7:
                if User.objects.filter(username=user).exists():
                    messages.success(request,"this user is already exsit!")
                    return redirect('signup')
        # create user
                else:
                    myuser = User.objects.create_user(username, email, password)
                    myuser.save()

                return render(request, 'login.html')
            else:
                messages.success(request,"password should be at least 8 characters")
                return redirect('signup')

        else:
            messages.success(request,"password does't match Please try again!")
            return redirect('signup')

        # create user
    else:
        return HttpResponse('Not Allowed')

    # return HttpResponse("Hello")
    return render(request, 'index.html')


def handlelogin(request):
    if request.method == 'POST':

        # Get Post Parameters
        loginusername = request.POST["loginusername"]
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)
        picuploaduser = smilingimagestable.objects.values_list('smileUserName',flat=True)
        v1 = list(picuploaduser)
        for i in v1:
            if loginusername == i:
                messages.success(request,("you already upload the picture"))
                return redirect('index')
            else:
                pass
        else:

            if user is not None:
                dj_login(request, user)
                return redirect('smile/dashboard')

            else:
                messages.success(request,("invalid credentials Please try again "))
                return redirect('login')
    return render(request, 'index.html')


def handlelogout(request):

    if request.method == 'GET':
        logout(request)
        return render(request, 'index.html')
    else:

        return render(request, 'index.html')


def testfunction(request):
    letter_count = 0
    var = request.GET.get('text', 'default')

    for char in var:
        letter_count += 1

    pramas = {'Var': letter_count}
    return render(request, 'testfunction.html', pramas)
