from django.contrib import admin
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
)
# Register your models here.
from .models import JobApplication


class JobApplicationAdmin(ModelAdmin):
    model = JobApplication
    menu_label = "Job Applications"
    menu_icon = "folder-inverse"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('jobpost', 'application_date', "email", "full_name", 'document', 'phone_number', 'about_yourself',
                    'when_can_you_start', 'monthly_salary_expectations', 'preferred_contract', 'consent')
    search_fields = ("email", "full_name",)


modeladmin_register(JobApplicationAdmin)

'''




'''