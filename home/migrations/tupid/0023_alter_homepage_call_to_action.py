# Generated by Django 3.2.9 on 2021-12-11 11:04

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_alter_homepage_call_to_action'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='call_to_action',
            field=wagtail.core.fields.StreamField([('call_to_action', wagtail.core.blocks.StructBlock([('button_text', wagtail.core.blocks.CharBlock(max_length=50, required=False)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.core.blocks.URLBlock(required=False))], blank=True, null=True))]),
        ),
    ]
