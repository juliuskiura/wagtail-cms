# Generated by Django 3.2.10 on 2021-12-21 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0012_auto_20211218_0646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelcontact',
            name='phone_number',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]
