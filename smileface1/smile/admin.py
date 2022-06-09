import imp
from django.contrib import admin

# Register your models here.
from .models import Smile , Category , product

admin.site.register(Smile)
admin.site.register(Category)
admin.site.register(product)

