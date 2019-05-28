from django import template
import datetime
from dateutil import parser

register = template.Library()

@register.filter(name='myDataFormat')
def myDataFormat(value, arg):
    try:
        if isinstance(value, datetime.datetime):
            return value.strftime(arg)
        else:
            datetime_struct = parser.parse(value)
            return datetime_struct.strftime(arg)
    except Exception as e:
        return e