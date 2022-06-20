from email import message
from multiprocessing import context
from tkinter import N
from django.core.mail import send_mail
from smileface1.settings import EMAIL_HOST_USER
import shutil
import os
import pdb
from django.conf import settings
from django.contrib import messages
from urllib import response
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Smile,profile
import matplotlib.pyplot as plt

from smileface1 import settings
from .forms import smileSubmitForm
import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY


def index(request):
    # return HttpResponse("Hello")
    return render(request, 'smile/index.html')


def dashboard(request):

    if request.user.is_superuser:
         smileImages = Smile.objects.all()
         #images = Smile.objects.aggregate(Count('smileImage'))
         images = Smile.objects.values_list('smileImage', flat=True).count()
         context = {
                "silmedata": smileImages,
                 "users_count": smileImages.count,
                 'images' :  images
            }
         return render(request, 'smile/newadmin.html', context)

def UploadMozacimage(request):
    if request.user.is_authenticated:
        user=request.user.username      
        status=Smile.objects.filter(smileUserName=user).count()
        # data=profile.objects.get(FName=user)
        if status>1:
            messages.success(request,"you already upload the profile!")
            return render(request, 'test.html')
        else:
            form = smileSubmitForm()
            form = smileSubmitForm(
                initial={'smileUserName': request.user.username})
            context = {'form': form}
            return render(request, 'test.html', context)
    messages.success(request,"you are not user")
    return render(request, 'test.html')

def submitSmile(request):
    if request.method == 'POST':
        request.FILES['smileImage'].name = request.user.username + '.png'
        form = smileSubmitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return redirect('smile:pricingplan')


def pricingplan(request):
    my_context = {
        "key": settings.STRIPE_PUBLISHABLE_KEY
    }
    return render(request, 'test.html', my_context)


def chargestripe5doller(request):
    if request.method == 'POST':

        try:
            charge = stripe.Charge.create(
                amount=500,
                currency='usd',
                description='Payment Gateway',
                source=request.POST['stripeToken']
            )
        except stripe.error.CardError as e:
            # Problem with the card
            pass
        except stripe.error.RateLimitError as e:
            # Too many requests made to the API too quickly
            pass
        except stripe.error.InvalidRequestError as e:
            # Invalid parameters were supplied to Stripe API
            pass
        except stripe.error.AuthenticationError as e:
            # Authentication Error: Authentication with Stripe API failed (maybe you changed API keys recently)
            pass
        except stripe.error.APIConnectionError as e:
            # Network communication with Stripe failed
            pass
        except stripe.error.StripeError as e:
            # Stripe Error
            pass
        else:
            # success
            return render(request, 'charge.html')


def chargestripe10doller(request):
    if request.method == 'POST':

        try:
            charge = stripe.Charge.create(
                amount=1000,
                currency='usd',
                description='Payment Gateway',
                source=request.POST['stripeToken']
            )
        except stripe.error.CardError as e:
            # Problem with the card
            pass
        except stripe.error.RateLimitError as e:
            # Too many requests made to the API too quickly
            pass
        except stripe.error.InvalidRequestError as e:
            # Invalid parameters were supplied to Stripe API
            pass
        except stripe.error.AuthenticationError as e:
            # Authentication Error: Authentication with Stripe API failed (maybe you changed API keys recently)
            pass
        except stripe.error.APIConnectionError as e:
            # Network communication with Stripe failed
            pass
        except stripe.error.StripeError as e:
            # Stripe Error
            pass
        else:
            # success
            return render(request, 'charge.html')


def chargestripe15doller(request):
    if request.method == 'POST':

        try:
            charge = stripe.Charge.create(
                amount=1500,
                currency='usd',
                description='Payment Gateway',
                source=request.POST['stripeToken']
            )
        except stripe.error.CardError as e:
            # Problem with the card
            pass
        except stripe.error.RateLimitError as e:
            # Too many requests made to the API too quickly
            pass
        except stripe.error.InvalidRequestError as e:
            # Invalid parameters were supplied to Stripe API
            pass
        except stripe.error.AuthenticationError as e:
            # Authentication Error: Authentication with Stripe API failed (maybe you changed API keys recently)
            pass
        except stripe.error.APIConnectionError as e:
            # Network communication with Stripe failed
            pass
        except stripe.error.StripeError as e:
            # Stripe Error
            pass
        else:
            # success
            return render(request, 'charge.html')

def approve(request, username):
    var1 = Smile.objects.filter(smileUserName=username).update(smile_Aprroval = True)
    if var1:
        approval_user=Smile.objects.get(smileUserName=username)
        approval_image = approval_user.smileImage
        source = os.path.join(settings.BASE_DIR) + "/media/"+f"{approval_image}"
        destination = os.path.join(settings.BASE_DIR)+f"/{approval_image}"
        shutil.copy(source, destination)
        messages.success(request,"The image is successfully approved")
        image_approve = "image_approve"    
        context = {
           "image_approve":image_approve
        }
        return render(request, "smile/newadmin.html",context)

    else:
        pass
        

    return render(request, 'charge.html')
    

def disapprove(request, username):
    query = username
    var1 =Smile.objects.filter(smileUserName=query).update(smile_Aprroval = False)
    to_send = User.objects.all()
    usera = User.objects.get(username=username)
    useremail = usera.email
    message = "your image not Approved plaese wait"
    from_email = EMAIL_HOST_USER
    to_recipent = [useremail, 'usmankhankh321@gmail.com']
    send_mail(
        username,
        message,
        from_email,
        to_recipent,
        fail_silently= False,
        )
    return render(request, 'charge.html')


def mozactemple(request):
    userInfor = Smile.objects.all()
    #images = Smile.objects.aggregate(Count('smileImage'))
    images = Smile.objects.values_list('smileImage', flat=True).count()
    context = {
         "mozactemplate":"true",
         "userInfor": userInfor,
         "users_count": userInfor.count,
         'images' :  images
            }
    return render(request, "smile/newadmin.html",context )




def generatemosac(request):
    os.system("python smileface1/test.py --target-image smileface1/test/test-data/a.jpg --input-folder  media/smile/images/ --grid-size 100 100 ")
    return HttpResponse("Generating Mosac")


def generatemosac2(request):
    os.system("python smileface1/test2.py --target-image smileface1/test/test-data/a.jpg --input-folder  media/smile/images/ --grid-size 100 100 ")
    return HttpResponse("Generating Mosac")


def newadmindashbord(request):
    if request.user.is_superuser:
         smileImages = Smile.objects.all()
         #images = Smile.objects.aggregate(Count('smileImage'))
         images = Smile.objects.values_list('smileImage', flat=True).count()
         context = {
                "newadmin":"true",
                "silmedata": smileImages,
                 "users_count": smileImages.count,
                 'images' :  images
            }
         return render(request, 'smile/newadmin.html', context)
    else:

        form = smileSubmitForm()
        form = smileSubmitForm(
            initial={'smileUserName': request.user.username})

        context = {'form': form}
        return render(request, 'smile/dashboard.html', context)


def CustomersImages(request):
    if request.user.is_superuser:
         CustomersInfo = Smile.objects.all()
         #images = Smile.objects.aggregate(Count('smileImage'))
         images = Smile.objects.values_list('smileImage', flat=True).count()
         context = {
                "CustomersInfo": CustomersInfo,
                 "Customer_count": CustomersInfo.count,
                 'images' :  images
            }
         return render(request, 'smile/newadmin.html', context)
    else:

        form = smileSubmitForm()
        form = smileSubmitForm(
            initial={'smileUserName': request.user.username})

        context = {'form': form}
        return render(request, 'smile/dashboard.html', context)
def userInfor(request):
    listOfUser=profile.objects.all()
    userInfor = Smile.objects.all()
    images = Smile.objects.values_list('smileImage', flat=True).count()
    context = {
                "userInfor": userInfor,
                 "users_count": userInfor.count,
                 'images' :  images,
                 "listOfUser":listOfUser
                 
            }
    return render(request, 'smile/newadmin.html', context)
    

def userIfind(request):
    if request.method == 'POST':
        username = request.POST["username"]
        CustomersInfo = Smile.objects.all()
         #images = Smile.objects.aggregate(Count('smileImage'))
        images = Smile.objects.values_list('smileImage', flat=True).count()
        userIfind_data = Smile.objects.filter(smileUserName=username).values()
        context = {
                "userIfind_data": userIfind_data,
                 "CustomersInfo": CustomersInfo,
                 "users_count": CustomersInfo.count,
                 'images' :  images
            }
        return render(request, 'smile/newadmin.html', context)
    else:
        return render(request, 'smile/newadmin.html')


        


    

