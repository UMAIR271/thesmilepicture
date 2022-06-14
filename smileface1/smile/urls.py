"""smileface1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
app_name = 'smile'

urlpatterns = [

    path('', views.index, name='ShopHome'),
    path('newadmindashbord', views.newadmindashbord, name='newadmindashbord'),
    path('UploadMozacimage', views.UploadMozacimage, name='UploadMozacimage'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('pricingplan', views.pricingplan, name='pricingplan'),
    path('chargestripe5doller', views.chargestripe5doller,
         name='chargestripe5doller'),
    path('chargestripe10doller', views.chargestripe10doller,
         name='chargestripe10doller'),
    path('chargestripe15doller', views.chargestripe15doller,
         name='chargestripe15doller'),
    path('submitSmile', views.submitSmile, name='submitSmile'),
    path('approve/<str:username>/', views.approve, name='approve'),
    path('disapprove/<str:username>/', views.disapprove, name='disapprove'),
    path('generatemosac', views.generatemosac, name='generatemosac'),
    path('generatemosac2', views.generatemosac2, name='generatemosac2'),
    path('userInfor', views.userInfor, name='userInfor'),
    path('userIfind', views.userIfind, name='userIfind'),


]
