# Generated by Django 3.2.9 on 2021-12-11 21:13

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0032_auto_20211211_1300'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='cta_1_text',
            new_name='first_cta_text',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='cta_2_text',
            new_name='second_cta_text',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='cta_1_page',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='cta_2_page',
        ),
        migrations.AddField(
            model_name='homepage',
            name='first_cta_page',
            field=wagtail.core.fields.StreamField([('first_cta_page', wagtail.core.blocks.PageChooserBlock(required=False))], blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='second_cta_page',
            field=wagtail.core.fields.StreamField([('second_cta_page', wagtail.core.blocks.PageChooserBlock(required=False))], blank=True, null=True),
        ),
    ]