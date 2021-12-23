from django.db import models
from wagtail.core.fields import StreamField
from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import (
    FieldPanel, 
    StreamFieldPanel,
     MultiFieldPanel, 
     InlinePanel)
from modelcluster.fields import ParentalKey
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core import blocks

from blog.models import ArticleDetails


class HomePageCarousel(Orderable):
    page = ParentalKey('home.HomePage', related_name = 'carousel')
    carousel_title = models.CharField(
        max_length=50, blank=False, null=True)
    carousel_content = StreamField([
        ('carousel_content', blocks.RichTextBlock()),

    ])

    carousel_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('carousel_title'),
        StreamFieldPanel('carousel_content'),
        ImageChooserPanel('carousel_image'),
    ]




class HomePage(Page):  
    '''
    Home page configuration 
    '''
    max_count = 1
    
    templates = 'home/home_page.html'
    subpage_types = ['blog.BlogArticlesList',
                     'services.ServicePage', 'contact.ContactPage', 'subscriptions.SubscriptionPage', 'careers.CareerListPage', 'policies.PolicyPage']
    

    banner_intro_small = models.CharField(max_length=50, blank=False, null=True)
    banner_header = models.CharField(max_length=50, blank=False, null=True)
    contact_section_heading = models.CharField(max_length=50, blank=False, null=True)
    contact_section_para = models.TextField(blank=False, null=True) 
    first_article_link = models.ForeignKey(
        'blog.ArticleDetails', null=True, blank=True, related_name='firstarticle', on_delete=models.RESTRICT)
   
    second_article_link = models.ForeignKey(
        'blog.ArticleDetails', null=True, blank=True, related_name='secondarticle', on_delete=models.RESTRICT)
   


    video_link = StreamField([       
       ( 'embed', EmbedBlock(max_width=800, max_height=400))
      
    ],
        null=True,
        blank=True,
    )

   
    

    content_panels = Page.content_panels + [
        MultiFieldPanel([            
            FieldPanel('banner_intro_small'),
            FieldPanel('banner_header'), 
           
           
          
        ], heading='Banner Container Options'),        

        MultiFieldPanel([
            StreamFieldPanel('video_link'),
        ], heading='Video Container Options'),

         MultiFieldPanel([
            FieldPanel('first_article_link'),
            FieldPanel('second_article_link'),
        ], heading='Home Page Articles'),


        MultiFieldPanel([
            InlinePanel('carousel', label='New Carousel contents'),
        ], heading='Carousel Container Options'),
       
       
        MultiFieldPanel([
            FieldPanel('contact_section_heading'),
            FieldPanel('contact_section_para'),
        ], heading='Contact Form Section Container'),
        
    ]
        




