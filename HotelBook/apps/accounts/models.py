from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)

    email = models.EmailField(blank=False)

    STATUS_SET = (
        ('U', 'User'),
        ('O', 'Owner'),
    )
    status = models.CharField(max_length=1, choices=STATUS_SET)

    SEX_SET = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    sex = models.CharField(max_length=1, choices=SEX_SET)

    phone = models.CharField(max_length=20)
    date_of_birth = models.DateField(null=True, blank=True, )
    home_address = models.CharField(max_length=150)

    def __str__(self):
        return self.last_name + ' ' + self.first_name
