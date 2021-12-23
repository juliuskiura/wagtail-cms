from typing import AbstractSet
from django.db import models
from django.http import JsonResponse
from django.shortcuts import render, redirect
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone

from wagtail.admin.edit_handlers import (
    FieldPanel, 
    InlinePanel, 
    FieldRowPanel,
    MultiFieldPanel
)
from modelcluster.fields import ParentalKey
from wagtail.core.fields import RichTextField
from wagtail.contrib.forms.models import (
    AbstractEmailForm, 
    AbstractFormField, 
    AbstractFormSubmission
    )

# Create your models here.
class FormField(AbstractFormField):
    page = ParentalKey(
        'ContactPage',
        on_delete= models.CASCADE,
        related_name= 'form_fields'

    )

 

class ContactPage(AbstractEmailForm):
    template = 'contact/contact_page.html'
    max_count = 1
    subpage_types = []
    banner_intro_small = models.CharField(
        max_length=50, blank=False, null=True)
    banner_header = models.CharField(max_length=50, blank=False, null=True)
    contact_form_para = models.TextField(blank=False, null=True)

    


    content_panels = AbstractEmailForm.content_panels + [
        MultiFieldPanel([
            FieldPanel('banner_intro_small'),
            FieldPanel('banner_header')],
            heading='Banner Section Container'
            ),

        MultiFieldPanel([
        FieldPanel('contact_form_para'),
        ], 

        heading='Contact Page Bottom Text'),


        InlinePanel('form_fields', label='Form Fields'),  


        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname='col6'),
                FieldPanel('to_address', classname='col6'),
            ]),
        FieldPanel('subject'),
        ], heading='Contact Us Page Settings')

    ] 
    



class ModelContact(models.Model):
   
    date_added = models.DateTimeField(
        default=timezone.now, null=True, blank=True)
    full_name = models.CharField(max_length=100)
    e_mail = models.EmailField(max_length=100)    
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    business = models.CharField(max_length=100)
    message = models.TextField()


    def __str__(self):
        return self.full_name

