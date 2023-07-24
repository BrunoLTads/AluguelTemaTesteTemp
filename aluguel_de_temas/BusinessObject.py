from django.db import models
from .models import *
from .views import *
from datetime import datetime


class BusinessObject:
    def calculardesconto(self,client_id):
        client_id = Client.objects.get(pk=client_id)
        if client_id.rents.count() > 1:
            #return Theme.price == Theme.price - (Theme.price * 0.1) MEU DEUS, MEU SENHOR, ME AJUDE, POR FAVOR
            return Theme.price - 0.1
        else:
            return 0
            #return Theme.price
    
    def descontodata(data):
        data = datetime.strptime(data, '%Y-%m-%d')
        if data.weekday() < 0 and data.weekday() > 5:
            return Theme.price - 0.40
        else:
            return 0