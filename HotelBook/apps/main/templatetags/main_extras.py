import datetime

from django import template

register = template.Library()


@register.simple_tag
def current_time():
    return datetime.datetime.now().time().isoformat(timespec='seconds')
