import imp
from django.contrib import admin

# Register your models here.
from .models import Smile

admin.site.register(Smile)

