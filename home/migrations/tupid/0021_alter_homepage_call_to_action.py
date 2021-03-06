# Generated by Django 3.2.9 on 2021-12-11 10:59

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_homepage_call_to_action'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='call_to_action',
            field=wagtail.core.fields.StreamField([('cta', wagtail.core.blocks.StructBlock([('button_text', wagtail.core.blocks.CharBlock(default='Learn more', max_length=50, required=False)), ('button_page', wagtail.core.blocks.PageChooserBlock(default='', required=False)), ('button_url', wagtail.core.blocks.URLBlock(default='', required=False))], blank=True, null=True))]),
        ),
    ]
