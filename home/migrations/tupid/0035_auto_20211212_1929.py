# Generated by Django 3.2.9 on 2021-12-12 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('home', '0034_homepage_cta_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='first_cta_text',
        ),
        migrations.AddField(
            model_name='homepage',
            name='myfirst_cta',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='related_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='first_cta', to='wagtailcore.page'),
        ),
    ]
