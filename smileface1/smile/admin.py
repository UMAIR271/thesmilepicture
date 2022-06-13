import imp
from django.contrib import admin

# Register your models here.
from .models import Smile, profile

admin.site.register(Smile)
admin.site.register(profile)


