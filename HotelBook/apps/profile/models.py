from django.contrib.auth.models import User, Group
from django.core import mail
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from HotelBook import settings


class Profile(models.Model):
    """Model for profile of user
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    SEX_SET = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    sex = models.CharField(max_length=1, choices=SEX_SET)

    phone = models.CharField(max_length=20)
    date_of_birth = models.DateField(null=True, blank=True, )
    home_address = models.CharField(max_length=150)

    SUBS_SET = (
        ('N', 'None'),
        ('H', 'Subscribe to new Hotels'),
    )
    subscription = models.CharField(max_length=1,
                                    choices=SUBS_SET, default='N')

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.groups.add(Group.objects.get(name='common users'))
        subject = 'Welcome!'
        html_message = render_to_string('emails/greeting.html',
                                        {'username': instance.username})
        plain_message = strip_tags(html_message)
        from_email = settings.DEFAULT_FROM_EMAIL
        to = instance.email

        mail.send_mail(subject, plain_message,
                       from_email, [to], html_message=html_message)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
