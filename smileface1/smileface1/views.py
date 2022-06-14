# I have created this website.


import argparse
from email.policy import default
from multiprocessing import context
import os
from webbrowser import get
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
from smile.code import generate_code
from smile.models import profile
import test as mosaci


def index(request):
    if request.user.is_superuser:
        smileImages = smilingimagestable.objects.all()
         #images = Smile.objects.aggregate(Count('smileImage'))
        images = smilingimagestable.objects.values_list('smileImage', flat=True).count()
        context = {
                "silmedata": smileImages,
                 "users_count": smileImages.count,
                 'images' :  images
            }
        return render(request, 'smile/newadmin.html', context)
    
    else:
        if request.user.is_authenticated:
            print("enter")
            if request.method == "GET":
                user=request.user.username
                print(user)      
                data=profile.objects.get(FName=user)
                context = {
                    'data':data
                }
                return render(request, 'test.html', context)


        if request.method == "POST":
            FirstName = request.POST["FirstName"]
            LastName = request.POST["LastName"]
            email = request.POST['email']
            phone = request.POST['phone']
            ReferalCode = request.POST['ReferalCode']
            profileimage = request.POST['profileimage']
            # if profile.objects.filter(FName=FirstName).exists():
            #     messages.success(request,"you already create the profile!")
            #     return render(request, 'test.html')
            # else:
            userid= ''
            data=User.objects.filter(username=FirstName).values()
            for i in data:
                id = i['id']
                userid=id
            userinstant = User.objects.get(id=userid)
            profile_obj = profile.objects.update(user_id=userinstant,LName=LastName,Phone=phone,profile_image=profileimage,)
            profile_data= profile.objects.filter(FName=FirstName).values()
            print(profile_data)
            print(type(profile_data))
            context={
                    'profile_data':profile_data
                }
            return render(request, 'test.html',context)

def status(request):
     if request.user.is_authenticated:
        user=request.user.username
        print(user)      
        status=smilingimagestable.objects.get(smileUserName=user)
        data1=profile.objects.get(FName=user)

        context={
            "status":status,
            "data1":data1
        }

        return render(request,'test.html',context)

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
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        checkCode = request.POST['referal']
        # Checks
        if password == password2:
            if len(password) >2:
                if User.objects.filter(username=user).exists():
                    messages.success(request,"this user is already exsit!")
                    return redirect('signup')
        # create user
                else:
                    if checkCode:
                        referal_obj=profile.objects.filter(referal_code=checkCode,).get()
                        point = referal_obj.points
                        point = point +1
                        print(point)
                        user = profile.objects.filter(FName=referal_obj).update(points=point)
                        myuser = User.objects.create_user(username, email, password)
                        myuser.save()
                        user= myuser.username
                        userid= ''
                        data=User.objects.filter(username=user).values()
                        for i in data:
                            id = i['id']
                            userid=id

                        userinstant = User.objects.get(id=userid)
                        code=generate_code()
                        profile_obj = profile.objects.create(FName=username,user_id= userinstant, email=email, referal_code=code)
                        profile_obj.save()

                    else:
                        myuser = User.objects.create_user(username, email, password)
                        myuser.save()
                        user= myuser.username
                        userid= ''
                        data=User.objects.filter(username=user).values()
                        for i in data:
                            id = i['id']
                            userid=id

                        userinstant = User.objects.get(id=userid)
                        code=generate_code()
                        profile_obj = profile.objects.create(FName=username,user_id= userinstant, email=email, referal_code=code)
                        profile_obj.save()

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
        print(loginusername,loginpassword)
        user = authenticate(username=loginusername, password=loginpassword)
        print(user)
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
                print("Checking User Name")
                return redirect('index')

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


def userDashbord(request):
    return render(request, 'test.html')