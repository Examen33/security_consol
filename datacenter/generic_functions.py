import datetime
from django.utils.timezone import localtime


def get_duration(visit):
    if visit.leaved_at:
        return visit.leaved_at - visit.entered_at
    else:
        return localtime() - visit.entered_at


def format_duration(duration):
    format_time = datetime.timedelta(seconds=int(duration.total_seconds()))
    return format_time


def is_visit_long(duration, minutes=60):
    sec_in_min = 60
    return int(duration.total_seconds() / sec_in_min) > minutes