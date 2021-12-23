from django.contrib import admin
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
)
# Register your models here.
from .models import ModelContact


class ModelContactAdmin(ModelAdmin):
    model = ModelContact
    menu_label = "Contact Forms"
    menu_icon = "mail"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('date_added', 'full_name',
                    "phone_number", "business", 'message')
    search_fields = ("email", "full_name",)


modeladmin_register(ModelContactAdmin)
