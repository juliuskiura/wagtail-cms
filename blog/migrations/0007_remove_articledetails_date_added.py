# Generated by Django 3.2.9 on 2021-12-10 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20211210_0824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articledetails',
            name='date_added',
        ),
    ]
