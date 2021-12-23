
from django.db import models


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
)



class FormField(AbstractFormField):
    page = ParentalKey(
        'SubscriptionPage',
        on_delete=models.CASCADE,
        related_name='form_fields'

    )


class SubscriptionPage(AbstractEmailForm):
    template = 'subscriptions/subscription_page.html'
    max_count =1
    subpage_types = []
    content_panels = AbstractEmailForm.content_panels + [       
        InlinePanel('form_fields', label='Subscription Fields'),


        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname='col6'),
                FieldPanel('to_address', classname='col6'),
            ]),            
        ], heading='Subscription Form')

    ]
