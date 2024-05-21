"""
ASGI config for django_backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

# from chat.consumers import ChatConsumer
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
# import chat.routing
import tasks.routing
#import chat.routing
#import tasks.routing
from django.urls import path
import logging

# logger = logging.getLogger('django')
# logger.info("ASGI application loaded.")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_backend.settings')

# application = get_asgi_application()
application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            # chat.routing.websocket_urlpatterns +
            tasks.routing.websocket_urlpatterns
        )
    ),
})

# + tasks.routing.ws_urpatterns,
# tasks.routing.ws_urpatterns