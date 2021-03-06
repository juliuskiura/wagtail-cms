from django.db import models
from django.db.models.fields import URLField
from django_extensions.db.fields import AutoSlugField
from wagtail.admin.edit_handlers import (
    MultiFieldPanel,
    InlinePanel,
    FieldPanel,
    PageChooserPanel
)
from wagtail.snippets.models import register_snippet
from wagtail.core.models import Orderable
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel


# Create your models here.
class MenuItem(Orderable):
    link_title =models.CharField(blank=True, null=True, max_length=50)
    link_url =models.CharField(blank=True, null=True, max_length=250)
    
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True, blank=True,
        on_delete=models.CASCADE,
    )
    open_in_new_tab = models.BooleanField(default=False, blank=True, null=True)

    page = ParentalKey('Menu', related_name='menu_items')

    panels = [
        FieldPanel('link_title'),
        FieldPanel('link_url'),
        PageChooserPanel('link_page'),
        FieldPanel('open_in_new_tab'),
    ]

    def __str__(self):
        return self.link_title

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_url:
            return self.link_url
        else:
            return '#'

    @property
    def title(self):
        if self.link_page and not self.link_title:
            return self.link_page.title
        elif self.link_title:
            return self.link_title
        else:
            return 'Menu Title Missing'






@register_snippet
class Menu(ClusterableModel):
    title =models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title', editable=True)

    panels = [
        MultiFieldPanel([
            FieldPanel('title'),
            FieldPanel('slug'),            
        ], heading='Menu'),
        InlinePanel('menu_items', label='Menu Items')
    ]

    def __str__(self):
        return self.title






class MegaMenuItem(Orderable):
    parent_link = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='menuchildren')
    link_title = models.CharField(blank=True, null=True, max_length=50)
    link_url = models.CharField(blank=True, null=True, max_length=250)

    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True, blank=True,
        on_delete=models.CASCADE,
    )
    open_in_new_tab = models.BooleanField(default=False, blank=True, null=True)

    page = ParentalKey('MegaMenu', related_name='mega_menu_items')
    panels = [
        FieldPanel('parent_link'),
        FieldPanel('link_title'),
        FieldPanel('link_url'),
        PageChooserPanel('link_page'),
        FieldPanel('open_in_new_tab'),
    ]



@register_snippet
class MegaMenu(ClusterableModel):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title', editable=True)

    panels = [
        MultiFieldPanel([
            FieldPanel('title'),
            FieldPanel('slug')
        ]),
        InlinePanel('mega_menu_items', label='Mega Menu Items')
    ]

    def __str__(self):
        return self.title
