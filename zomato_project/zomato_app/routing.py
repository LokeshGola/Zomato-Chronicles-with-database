# zomato_project/routing.py
from django.urls import re_path
from zomato_app import consumers

from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from zomato_project import routing as zomato_routing


websocket_urlpatterns = [
    re_path(r'ws/order_status/$', consumers.OrderStatusConsumer.as_asgi()),
]


application = ProtocolTypeRouter({
    "websocket": URLRouter(
        zomato_routing.websocket_urlpatterns
    ),
})

