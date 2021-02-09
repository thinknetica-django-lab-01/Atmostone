from django.contrib.auth.models import User, Group
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    SEX_SET = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    sex = models.CharField(max_length=1, choices=SEX_SET)

    phone = models.CharField(max_length=20)
    date_of_birth = models.DateField(null=True, blank=True, )
    home_address = models.CharField(max_length=150)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.groups.add(Group.objects.get(name='common users'))


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()