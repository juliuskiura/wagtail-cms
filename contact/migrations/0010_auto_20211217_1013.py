# Generated by Django 3.2.10 on 2021-12-17 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0009_alter_modelcontact_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactpage',
            name='banner_header',
        ),
        migrations.RemoveField(
            model_name='contactpage',
            name='banner_intro_small',
        ),
        migrations.RemoveField(
            model_name='contactpage',
            name='contact_form_para',
        ),
    ]
