from django.contrib import admin
# from wagtail.wagtailimages.formats import unregister_image_format
from wagtail.images.formats import unregister_image_format, register_image_format, Format


register_image_format(Format('left_wrapped', ('Left-aligned-wrapped'), 'richtext-image left-wrapped', 'width-500'))
register_image_format(Format('right_wrapped', ('Right-aligned-wrapped'), 'richtext-image right-wrapped', 'width-500'))

# Register your models here.
