import datetime

from django.core import mail
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.html import strip_tags

from HotelBook import settings
from HotelBook.celery import app
from apps import main, profile


@app.task
def send_emails_for_subscibers(subject, plain_message, from_email, subscribers, html_message):
    mail.send_mail(subject, plain_message, from_email, subscribers, html_message=html_message)


@app.task
def weekly_updates_emails():
    new_hotels = [hotel for hotel in
                  main.models.Hotel.objects.filter(created_at__gte=timezone.now() - datetime.timedelta(days=7))]
    subscribers = [prof.user.email for prof in profile.models.Profile.objects.filter(subscription='H')]
    html_message = render_to_string('emails/week_hotels.html', {'hotels': new_hotels})
    mail.send_mail('Check new hotels for the last week',
                   strip_tags(html_message),
                   settings.DEFAULT_FROM_EMAIL,
                   subscribers, html_message=html_message)
