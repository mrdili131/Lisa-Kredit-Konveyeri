from django.contrib import admin
from .models import Client, Application, Credit

admin.site.register([Client, Application, Credit])
