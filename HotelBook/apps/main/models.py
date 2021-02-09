from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from apps.profile.models import User


class Country(models.Model):
    title = models.CharField(max_length=150, blank=False)

    def __str__(self):
        return self.title


class City(models.Model):
    title = models.CharField(max_length=150, blank=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return self.title


class HotelFeature(models.Model):
    title = models.CharField(max_length=150, blank=False)

    def __str__(self):
        return self.title


class RoomFeature(models.Model):
    title = models.CharField(max_length=150, blank=False)

    def __str__(self):
        return self.title


class Hotel(models.Model):
    title = models.CharField(max_length=150, blank=False)

    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=False)
    address = models.CharField(max_length=150, blank=False)

    rating = models.DecimalField(max_digits=4, decimal_places=2,
                                 validators=[MinValueValidator(0),
                                             MaxValueValidator(10)], blank=False)

    STARS_SET = (
        ('N', 'No stars'),
        ('1', '1 stars'),
        ('2', '2 stars'),
        ('3', '3 stars'),
        ('4', '4 stars'),
        ('5', '5 stars'),
    )
    stars = models.CharField(max_length=1, choices=STARS_SET, blank=False)
    features = models.ManyToManyField(HotelFeature)

    def __str__(self):
        return self.title


class Room(models.Model):
    room_type = models.CharField(max_length=150, blank=False)
    room_square = models.DecimalField(decimal_places=1, max_digits=10, blank=False)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, blank=False)
    room_features = models.ManyToManyField(RoomFeature)
    persons = models.IntegerField(blank=False)

    price = models.DecimalField(decimal_places=2, max_digits=10, blank=False)

    def __str__(self):
        return self.room_type + ' room. ' + self.hotel.title + ' hotel'


class Order(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=False)
    arrival_date = models.DateField(blank=False)
    departure_date = models.DateField(blank=False)

    @property
    def amount(self):
        return (self.departure_date - self.arrival_date).days * self.room.price

    def __str__(self):
        return self.person.last_name + ' ' + self.person.first_name + '. ' + self.room.hotel.title + ' hotel. ' + self.room.room_type + ' room. ' + str(
            self.amount) + ' RUB.'
