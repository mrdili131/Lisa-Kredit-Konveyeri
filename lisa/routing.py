from django.urls import path

from . import consumers

ws_urlpatterns = [
    path('ws/',consumers.WebSock.as_asgi())
]