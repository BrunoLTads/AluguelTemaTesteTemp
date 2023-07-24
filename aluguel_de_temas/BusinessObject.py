from django.db import models
from .models import *
from .views import *
from datetime import datetime


class BusinessObject:
    def calculardesconto(self,client_id):
        client_id = Client.objects.get(pk=client_id)
        if client_id.rents.count() > 1:
            #return Theme.price == Theme.price - (Theme.price * 0.1)
            return 0.1
        else:
            return 1
            #return Theme.price