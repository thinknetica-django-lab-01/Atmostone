from django.core import mail

from HotelBook.celery import app


@app.task
def send_emails_for_subscibers(subject, plain_message, from_email, subscribers, html_message):
    mail.send_mail(subject, plain_message, from_email, subscribers, html_message=html_message)
