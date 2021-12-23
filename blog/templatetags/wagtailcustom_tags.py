from django import template
from django.utils.safestring import mark_safe
from django.utils.html import strip_tags
from wagtail.core.rich_text import RichText

register = template.Library()


@register.filter
def clean_block(value):
   
    try:
        plain_text = strip_tags(value)
    except:
        plain_text = 'Template error'
    
    return plain_text
