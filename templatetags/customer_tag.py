from django import template
import re

register = template.Library()


@register.filter(name="myfilter", is_safe=True, needs_autoescape=True)
def myfilter(value, autoescape=True):
    result = re
    return result
