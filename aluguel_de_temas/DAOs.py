from .models import *

class DAOsClient:
    def listarclient():
        client = Client.objects.all()
        return client
    
    def salvarclient(name, cpf):
        c = Client(name=name,
                   cpf=cpf)
        c.save()
        
    def atualizarclient(name, cpf, id):
        c = Client.objects.get(pk=id)
        c.name = name
        c.cpf = cpf
        c.save()
    
    def deletarclient(id):
        c = Client.objects.get(pk=id)
        c.delete()
    

class DAOsItem:
    def listaritem():
        item = Item.objects.all()
        return item 
    
    def salvaritem(name, description):
        i = Item(name=name, 
                 description=description)
        i.save()
    
    def deletaritem(id):
        i = Item.objects.get(pk=id)
        i.delete()
    
    def atualizaritem(name, description, id):
        i = Item.objects.get(pk=id)
        i.name = name
        i.description = description
        i.save()

class DaosRent:
    def listarrent():
        rent = Rent.objects.all()
        return rent
    
    def salvarrent(street, number, complement, district, city, state, date, start_hours, end_hours, client_id, theme_id):
        a = Address(street=street,
                    number=number,
                    complement=complement,
                    district=district,
                    city=city,
                    state=state)
        a.save()

        r = Rent(date=date,
                 start_hours=start_hours,
                 end_hours=end_hours,
                 client_id=client_id,
                 theme_id=theme_id,
                 address = a)
        
        r.price = r.theme.price

        r.save()
    
    def deletarrent(id):
        r = Rent.objects.get(pk=id)
        r.delete()
    
    def atualizarrent(street, number, complement, district, city, state, date, start_hours, end_hours, client_id, theme_id, id):
        a = Address.objects.get(pk=id)
        a.street = street
        a.number = number
        a.complement = complement
        a.district = district
        a.city = city
        a.state = state
        a.save()

        r = Rent.objects.get(pk=id)
        r.date = date
        r.start_hours = start_hours
        r.end_hours = end_hours
        r.client = client_id
        r.theme = theme_id
        r.address = a
        r.save()



