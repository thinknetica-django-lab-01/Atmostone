from channels.generic.websocket import WebsocketConsumer
import json

from apps.main.models import Hotel


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(text_data=json.dumps({
            'message': 'Welcome! To check if hotel is available type: "A#<Hotel name>"'
        }))

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        if message.startswith('A#'):
            message = message.split('#')[1]
            try:
                Hotel.objects.get(title=message)
                message = 'This hotel is available'
            except Exception:
                message = 'This hotel is not available'
        else:
            message = 'To check if hotel is available type: "A#<Hotel name>"'
        self.send(text_data=json.dumps({
            'message': message
        }))
