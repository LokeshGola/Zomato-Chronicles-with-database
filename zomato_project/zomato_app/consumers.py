# zomato_app/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class OrderStatusConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def update_status(self, event):
        status = event['status']
        await self.send(text_data=json.dumps({
            'status': status
        }))
