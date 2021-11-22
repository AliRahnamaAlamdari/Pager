import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Orders
from RestaurantApp.models import AppUser
from .serializers import OrderSerializer
class ChatConsumer(WebsocketConsumer):
    

    def order_scan(self ,data):
        order =Orders.objects.get(pk = data["order_id"])
        user = AppUser.objects.get(pk=data["user_id"])
        order.User = user
        order.save()
        order_serializer = OrderSerializer(instance=order)
        self.send_to_other(
            {
                "order" : order_serializer.data,
                "command" : "Get order from server."
            }
        )

    def food_prepared(self , data):
        order =Orders.objects.get(pk = data["order_id"])
        order.is_prepaerd = True
        order.save()
        self.send_to_other(
            {
                "command" :"food is prepared."
            }
        )




    commands = {
        
        "order_scan": order_scan,
        "food_prepared": food_prepared
    
    }


    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_dict = json.loads(text_data)
        message = text_data_dict['message']

        # Send message to room group
        self.commands[message](self, text_data_dict)
        


    def send_to_other(self, message):
        
        command = message.get("command", None)
        order = message.get("order" , None)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': command,
                'order' : order,
                'sender_channel_name': self.channel_name
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        if event["order"] is None:
            if self.channel_name != event['sender_channel_name']:
                self.send(text_data=json.dumps({
                    'message': message
                }))
        else:
            if self.channel_name == event['sender_channel_name']:
                self.send(text_data=json.dumps({
                    'message': message,
                    'order' : event["order"]
                    
                }))
        # Send message to WebSocket
        