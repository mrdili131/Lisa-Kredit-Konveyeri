import json
from channels.generic.websocket import WebsocketConsumer
from .utils import save_to_db

class WebSock(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(text_data=json.dumps({"backend":"Welcome bro!"}))

    def close(self,close_code):
        pass
        
    def receive(self,text_data):
        from .models import Credit
        data = json.loads(text_data)
        check = Credit.objects.filter(id=data['credit-data']['credit_id']).first()
        if check:
            credit = Credit.objects.get(id=data['credit-data']['credit_id'])
            if int(data['credit-data']['amount']) and int(data['credit-data']['amount']) <= credit.application.limit_amount:
                self.send(text_data=json.dumps(save_to_db(data)))