# Generated by Django 3.2.10 on 2021-12-23 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('policies', '0002_alter_policypage_text_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='policypage',
            name='banner_header',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='policypage',
            name='banner_intro_small',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
