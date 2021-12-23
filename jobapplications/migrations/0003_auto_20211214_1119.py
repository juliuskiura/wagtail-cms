# Generated by Django 3.2.10 on 2021-12-14 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('wagtailcore', '0066_collection_management_permissions'),
        ('menus', '0001_initial'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('jobapplications', '0002_auto_20211214_1112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formpage',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='FormField',
        ),
        migrations.DeleteModel(
            name='FormPage',
        ),
    ]
