# Generated by Django 3.2.10 on 2021-12-14 13:35

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('jobapplications', '0005_auto_20211214_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploaddocument',
            name='about_yourself',
            field=models.TextField(default='me'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uploaddocument',
            name='consent',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uploaddocument',
            name='monthly_salary_expectations',
            field=models.DecimalField(decimal_places=2, default=1000, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uploaddocument',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default='254722312723', max_length=128, region=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uploaddocument',
            name='preferred_contract',
            field=models.CharField(default='non', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uploaddocument',
            name='when_can_you_start',
            field=models.TextField(default='now'),
            preserve_default=False,
        ),
    ]
