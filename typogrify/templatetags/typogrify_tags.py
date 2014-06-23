import calendar
from datetime import date, timedelta

from django import template
from django.conf import settings
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape
from django.utils.translation import ungettext, ugettext

import typogrify.filters as _filters

register = template.Library()


def smart_filter(fn):
    '''
    Escapes filter's content based on template autoescape mode and marks output as safe
    '''
    def wrapper(text, autoescape=None):
        if autoescape:
            esc = conditional_escape
        else:
            esc = lambda x: x

        return mark_safe(fn(esc(text)))
    wrapper.needs_autoescape = True

    register.filter(fn.__name__, wrapper)
    return wrapper


amp = smart_filter(_filters.amp)
caps = smart_filter(_filters.caps)
number_suffix = smart_filter(_filters.number_suffix)
initial_quotes = smart_filter(_filters.initial_quotes)
smartypants = smart_filter(_filters.smartypants)
titlecase = smart_filter(_filters.titlecase)
widont = smart_filter(_filters.widont)
typogrify = smart_filter(_filters.typogrify)


@register.filter
def fuzzydate(value, cutoff=180):
    """
    * takes a value (date) and cutoff (in days)

    If the date is within 1 day of Today:
        Returns
            'today'
            'yesterday'
            'tomorrow'

    If the date is within Today +/- the cutoff:
        Returns
            '2 months ago'
            'in 3 weeks'
            '2 years ago'
            etc.


    if this date is from the current year, but outside the cutoff:
        returns the value for 'CURRENT_YEAR_DATE_FORMAT' in settings if it exists.
        Otherwise returns:
            January 10th
            December 1st

    if the date is not from the current year and outside the cutoff:
        returns the value for 'DATE_FORMAT' in settings if it exists.
    """

    try:
        value = date(value.year, value.month, value.day)
    except AttributeError:
        # Passed value wasn't a date object
        return value
    except ValueError:
        # Date arguments out of range
        return value

    today = date.today()
    delta = value - today

    if delta.days == 0:
        return u"today"
    elif delta.days == -1:
        return u"yesterday"
    elif delta.days == 1:
        return u"tomorrow"

    chunks = (
        (365.0, lambda n: ungettext('year', 'years', n)),
        (30.0, lambda n: ungettext('month', 'months', n)),
        (7.0, lambda n: ungettext('week', 'weeks', n)),
        (1.0, lambda n: ungettext('day', 'days', n)),
    )

    if abs(delta.days) <= cutoff:
        for i, (chunk, name) in enumerate(chunks):
                if abs(delta.days) >= chunk:
                    count = abs(round(delta.days / chunk, 0))
                    break

        date_str = ugettext('%(number)d %(type)s') % {'number': count, 'type': name(count)}

        if delta.days > 0:
            return "in " + date_str
        else:
            return date_str + " ago"
    else:
        if value.year == today.year:
            format = getattr(settings, "CURRENT_YEAR_DATE_FORMAT", "F jS")
        else:
            format = getattr(settings, "DATE_FORMAT")

        return template.defaultfilters.date(value, format)
fuzzydate.is_safe = True


@register.filter
def super_fuzzydate(value):
    try:
        value = date(value.year, value.month, value.day)
    except AttributeError:
        # Passed value wasn't a date object
        return value
    except ValueError:
        # Date arguments out of range
        return value

    # today
    today = date.today()
    delta = value - today

    # get the easy values out of the way
    if delta.days == 0:
        return u"Today"
    elif delta.days == -1:
        return u"Yesterday"
    elif delta.days == 1:
        return u"Tomorrow"

    # if we're in the future...
    if value > today:
        end_of_week = today + timedelta(days=7 - today.isoweekday())
        if value <= end_of_week:
            # return the name of the day (Wednesday)
            return u'this %s' % template.defaultfilters.date(value, "l")

        end_of_next_week = end_of_week + timedelta(weeks=1)
        if value <= end_of_next_week:
            # return the name of the day(Next Wednesday)
            return u"next %s" % template.defaultfilters.date(value, "l")

        end_of_month = today + timedelta(calendar.monthrange(today.year, today.month)[1] - today.day)
        if value <= end_of_month:
            # return the number of weeks (in two weeks)
            if value <= end_of_next_week + timedelta(weeks=1):
                return u"in two weeks"
            elif value <= end_of_next_week + timedelta(weeks=2):
                return u"in three weeks"
            elif value <= end_of_next_week + timedelta(weeks=3):
                return u"in four weeks"
            elif value <= end_of_next_week + timedelta(weeks=4):
                return u"in five weeks"

        if today.month == 12:
            next_month = 1
        else:
            next_month = today.month + 1

        end_of_next_month = date(today.year, next_month, calendar.monthrange(today.year, today.month)[1])
        if value <= end_of_next_month:
            # if we're in next month
            return u'next month'

        # the last day of the year
        end_of_year = date(today.year, 12, 31)
        if value <= end_of_year:
            # return the month name (March)
            return template.defaultfilters.date(value, "F")

        # the last day of next year
        end_of_next_year = date(today.year + 1, 12, 31)
        if value <= end_of_next_year:
            return u'next %s' % template.defaultfilters.date(value, "F")

        return template.defaultfilters.date(value, "Y")
    else:
        # TODO add the past
        return fuzzydate(value)
super_fuzzydate.is_safe = True

@register.filter
def text_whole_number(value):
    """
    Takes a whole number, and if its less than 10, writes it out in text.

    english only for now.
    """

    try:
        value = int(value)
    except ValueError:
        # Not an int
        return value

    if value <= 10:
        if value == 1:
            value = "one"
        elif value == 2:
            value = "two"
        elif value == 3:
            value = "three"
        elif value == 4:
            value = "four"
        elif value == 5:
            value = "five"
        elif value == 6:
            value = "six"
        elif value == 7:
            value = "seven"
        elif value == 8:
            value = "eight"
        elif value == 9:
            value = "nine"
        elif value == 10:
            value = "ten"
    return value
text_whole_number.is_safe = True

def _test():
    import doctest
    doctest.testmod()


if __name__ == "__main__":
    _test()
