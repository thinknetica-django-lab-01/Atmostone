import datetime

from apps.profile.models import User
from apps.main.models import Hotel, City, HotelFeature, Order, Room

# Creating new hotel
h = Hotel(title='Novotel', city=City.objects.get(title='Moscow'),
          address='Moscow City', rating=9.2, stars='4')
h.save()

# Adding m2m field (all features)
feature = HotelFeature.objects.all()
h.features.set(feature)
h.save()

# Modifying m2m field (filtered feature)
feature = HotelFeature.objects.filter(title='Parking')
h.features.set(feature)
h.save()

# Creating new order
Order.objects.create(person=User.objects.get(username='admin'),
                     room=Room.objects.get(room_type='Single'),
                     arrival_date=datetime.date(2021, 1, 30),
                     departure_date=datetime.date(2021, 1, 31))



