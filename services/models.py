from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel
from wagtail.core import blocks

from streams import core_blocks

# Create your models here.


class ServicePage(Page):
    description = models.TextField(blank=False, null=True)
    content_panels = Page.content_panels + [
        FieldPanel('description'),
        
    ]
    subpage_types = ['services.GenericServicePage',]
    max_count = 1
   


class GenericServicePage(Page):
    

    '''
    Generic pages configuration 
    '''
    templates = 'services/generic_page.html'
    subpage_types = []

    banner_intro_small = models.CharField(
        max_length=50, blank=False, null=True)
    banner_header = models.CharField(max_length=50, blank=False, null=True)
    banner_para = models.TextField(blank=False, null=True)
    contact_section_heading = models.CharField(
        max_length=50, blank=False, null=True)
    contact_section_para = models.TextField(blank=False, null=True)

    container = StreamField([
        ('heading_and_paragraph', core_blocks.HeadingAndParagraphBlocks()),

    ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
        FieldPanel('banner_intro_small'),
        FieldPanel('banner_header'),
        FieldPanel('banner_para'),       
        ],  heading='Banner Section Container'),

        MultiFieldPanel([     
        StreamFieldPanel('container'),
        ],  heading='Services Section Container'),

        MultiFieldPanel([
            FieldPanel('contact_section_heading'),
            FieldPanel('contact_section_para'),
        ], heading='Contact Form Section Container'),
    ]
