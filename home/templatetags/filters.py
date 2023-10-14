from django import template
import datetime

register = template.Library()


@register.simple_tag
def current_time(format_string='%H:%M:%S'):
    now = datetime.datetime.now()
    right_now = now.strftime(format_string)
    return right_now
@register.filter
def cutter(value, arg):
    return f"{value[:arg]}..."


