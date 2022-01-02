from django.db import models
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel
from wagtail.core.models import PAGE_MODEL_CLASSES, Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from streams.core_blocks import ParagraphBlocks
# Create your models here.


class PolicyPage(Page):
    template = 'policies/policy_page.html'
    banner_intro_small = models.CharField(
        max_length=50, blank=False, null=True)
    banner_header = models.CharField(max_length=50, blank=False, null=True)

    container = StreamField(
        [
            ('text_content', ParagraphBlocks())
        ])


    subpage_types = []

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('banner_intro_small'),
            FieldPanel('banner_header'),
        ], heading='Banner Container Options'),

        MultiFieldPanel([
            StreamFieldPanel('container', ),
        ], heading='Policy Block Content')
        
    ]
