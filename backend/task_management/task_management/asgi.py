import os
import django
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_management.settings')
django.setup()

from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from lists.views import ListConsumer

websocket_urlpatterns = [
    path('ws/lists/', ListConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(
        websocket_urlpatterns
    ),
})