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
from distutils.ccompiler import show_compilers
import imp
from django.contrib import admin
from django.urls import path, include

from smile import urls
import smile
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin', admin.site.urls),
    path('index', views.index, name='index'),
    path('status', views.status, name='status'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('contactus', views.contactus, name='contactus'),
    path('mission', views.mission, name='mission'),
    path('', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('reasontosmile', views.reasontosmile, name='reasontosmile'),
    path('testfunction', views.testfunction, name='testfunction'),
    path('click', views.click, name='click'),
    path('handlesignup', views.handlesignup, name='handlesignup'),
    path('handlelogin', views.handlelogin, name='handlelogin'),
    path('handlelogout', views.handlelogout, name='handlelogout'),
    path('handlelogout', views.handlelogout, name='handlelogout'),
    path('smile/',  include(smile.urls, namespace='smile'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
