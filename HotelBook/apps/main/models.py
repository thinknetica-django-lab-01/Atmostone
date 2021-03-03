from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import decimal
from HotelBook import settings
from apps.main.tasks import send_emails_for_subscibers
from apps.profile.models import User, Profile
from django.contrib.postgres.fields import ArrayField


class Country(models.Model):
    """Model for countries
    """
    title = models.CharField(max_length=150, blank=False)

    def __str__(self) -> str:
        return self.title


class City(models.Model):
    """Model for cities
    """
    title = models.CharField(max_length=150, blank=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=False)

    def __str__(self) -> str:
        return self.title


class RoomFeature(models.Model):
    """Model for features of rooms
    """
    title = models.CharField(max_length=150, blank=False)

    def __str__(self) -> str:
        return self.title


class Hotel(models.Model):
    """Model for hotels
    """
    title = models.CharField(max_length=150, blank=False)

    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=False)
    address = models.CharField(max_length=150, blank=False)

    rating = models.DecimalField(max_digits=4, decimal_places=2,
                                 validators=[MinValueValidator(0),
                                             MaxValueValidator(10)],
                                 blank=False)

    STARS_SET = (
        ('N', 'No stars'),
        ('1', '1 stars'),
        ('2', '2 stars'),
        ('3', '3 stars'),
        ('4', '4 stars'),
        ('5', '5 stars'),
    )
    stars = models.CharField(max_length=1, choices=STARS_SET, blank=False)

    features = ArrayField(models.CharField(max_length=150), blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    views = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['-created_at']


class Room(models.Model):
    """Model for room in hotel
    """
    room_type = models.CharField(max_length=150, blank=False)
    room_square = models.DecimalField(decimal_places=1,
                                      max_digits=10, blank=False)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, blank=False)
    room_features = models.ManyToManyField(RoomFeature)
    persons = models.IntegerField(blank=False)

    price = models.DecimalField(decimal_places=2, max_digits=10, blank=False)

    def __str__(self) -> str:
        return self.room_type + ' room. ' + self.hotel.title + ' hotel'


class Order(models.Model):
    """Model for order of the room
    """
    person = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=False)
    arrival_date = models.DateField(blank=False)
    departure_date = models.DateField(blank=False)

    @property
    def amount(self) -> decimal.Decimal:
        """
        :return: Amount of money for whole order
        """
        return (self.departure_date - self.arrival_date).days * self.room.price

    def __str__(self) -> str:
        return self.person.last_name + ' ' + self.person.first_name + \
               '. ' + self.room.hotel.title + ' hotel. ' + \
               self.room.room_type + ' room. ' + str(
            self.amount) + ' RUB.'


@receiver(post_save, sender=Hotel)
def new_hotel_mailing(sender, instance, created, **kwargs):
    if created:
        subscribers = [profile.user.email for profile
                       in Profile.objects.filter(subscription='H')]
        subject = 'We got a new hotel for you!'
        html_message = render_to_string('emails/new_hotel.html',
                                        {'title': instance.title})
        plain_message = strip_tags(html_message)
        from_email = settings.DEFAULT_FROM_EMAIL
        send_emails_for_subscibers.delay(subject, plain_message,
                                         from_email, subscribers, html_message)
