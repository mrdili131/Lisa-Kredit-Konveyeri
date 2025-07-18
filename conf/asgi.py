import os
import django
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from lisa.routing import ws_urlpatterns


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')
django.setup()


application = ProtocolTypeRouter({
    "http":get_asgi_application(),
    "websocket":AuthMiddlewareStack(
        URLRouter(
            ws_urlpatterns
        )
    ),
})