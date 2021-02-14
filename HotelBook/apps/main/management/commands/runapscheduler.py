import logging
import datetime

from django.core import mail
from django.template.loader import render_to_string
from django.utils import timezone

from django.conf import settings

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django.utils.html import strip_tags
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution

from apps.main.models import Hotel
from apps.profile.models import Profile

logger = logging.getLogger(__name__)


def my_job():
    """This job send emails for subscribed users list of new hotels for the last week"""

    new_hotels = [hotel for hotel in Hotel.objects.filter(created_at__gte=timezone.now() - datetime.timedelta(days=7))]

    subscribers = [profile.user.email for profile in Profile.objects.filter(subscription='H')]

    html_message = render_to_string('emails/week_hotels.html', {'hotels': new_hotels})

    mail.send_mail('Check new hotels for the last week',
                   strip_tags(html_message),
                   settings.DEFAULT_FROM_EMAIL,
                   subscribers, html_message=html_message)


def delete_old_job_executions(max_age=604_800):
    """This job deletes all apscheduler job executions older than `max_age` from the database."""
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs apscheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            my_job,
            trigger=CronTrigger(day_of_week="sat", hour="12", minute="00"),
            id="my_job",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'my_job'.")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),
            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info(
            "Added weekly job: 'delete_old_job_executions'."
        )

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")
