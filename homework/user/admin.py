from django.contrib import admin

# Register your models here.
# user/admin.py
from django.contrib import admin
from .models import CustomUser

admin.site.register(CustomUser)
