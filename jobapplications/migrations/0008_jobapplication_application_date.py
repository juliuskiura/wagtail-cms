# Generated by Django 3.2.10 on 2021-12-14 14:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobapplications', '0007_rename_uploaddocument_jobapplication'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='application_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
