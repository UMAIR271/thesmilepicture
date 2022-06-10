from email import message
from django.core.mail import send_mail
from smileface1.settings import EMAIL_HOST_USER
import os
from django.conf import settings
from pyexpat.errors import messages
from urllib import response
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Smile
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
    else:

        form = smileSubmitForm()
        form = smileSubmitForm(
            initial={'smileUserName': request.user.username})

        context = {'form': form}
        return render(request, 'smile/dashboard.html', context)


def submitSmile(request):
    if request.method == 'POST':
        request.FILES['smileImage'].name = request.user.username + '.png'
        form = smileSubmitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return redirect('pricingplan')


def pricingplan(request):
    my_context = {
        "key": settings.STRIPE_PUBLISHABLE_KEY
    }
    return render(request, 'smile/pricingplan.html', my_context)


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
        plt.savefig(os.path.join(settings.BASE_DIR,f"{approval_image}"))
        print("umair")
    else:
        pass
        

    return render(request, 'charge.html')
    

def disapprove(request, username):
    query = username
    var1 =Smile.objects.filter(smileUserName=query).update(smile_Aprroval = False)
    to_send = User.objects.all()
    usera = User.objects.get(username=username)
    useremail = usera.email
    print(useremail)
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




def generatemosac(request):

    print("generating mosac")
    os.system("python smileface1/test.py --target-image smileface1/test/test-data/a.jpg --input-folder  media/smile/images/ --grid-size 100 100 ")
    return HttpResponse("Generating Mosac")


def generatemosac2(request):
    print("generating mosac")
    os.system("python smileface1/test2.py --target-image smileface1/test/test-data/a.jpg --input-folder  media/smile/images/ --grid-size 100 100 ")
    return HttpResponse("Generating Mosac")


def newadmindashbord(request):
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
    else:

        form = smileSubmitForm()
        form = smileSubmitForm(
            initial={'smileUserName': request.user.username})

        context = {'form': form}
        return render(request, 'smile/dashboard.html', context)


def userInfor(request):
    if request.user.is_superuser:
         userInfor = Smile.objects.all()
         #images = Smile.objects.aggregate(Count('smileImage'))
         images = Smile.objects.values_list('smileImage', flat=True).count()
         context = {
                "userInfor": userInfor,
                 "users_count": userInfor.count,
                 'images' :  images
            }
         return render(request, 'smile/newadmin.html', context)
    else:

        form = smileSubmitForm()
        form = smileSubmitForm(
            initial={'smileUserName': request.user.username})

        context = {'form': form}
        return render(request, 'smile/dashboard.html', context)


def userIfind(request):
    if request.method == 'POST':
        username = request.POST["username"]
        userInfor = Smile.objects.all()
         #images = Smile.objects.aggregate(Count('smileImage'))
        images = Smile.objects.values_list('smileImage', flat=True).count()
        data = Smile.objects.filter(smileUserName=username).values()
        print(data)
        context = {
                "data": data,
                 "userInfor": userInfor,
                 "users_count": userInfor.count,
                 'images' :  images
            }
        return render(request, 'smile/newadmin.html', context)
    else:
        return render(request, 'smile/newadmin.html')


        


    

