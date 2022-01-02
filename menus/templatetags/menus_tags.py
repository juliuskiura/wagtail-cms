from django import template

from ..models import Menu
from ..models import MegaMenu

register = template.Library()

@register.simple_tag()
def get_menu(slug):
    return Menu.objects.get(slug=slug)


