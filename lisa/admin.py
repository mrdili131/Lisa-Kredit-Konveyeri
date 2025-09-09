from django.contrib import admin
from .models import Client, Application, Credit, PhoneNumber

admin.site.register([Client, Application, Credit, PhoneNumber])
