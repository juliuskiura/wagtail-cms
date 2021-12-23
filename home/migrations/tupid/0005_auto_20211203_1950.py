# Generated by Django 3.2.9 on 2021-12-03 19:50

from django.db import migrations
import streams.core_blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20211203_1649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='content',
        ),
        migrations.AddField(
            model_name='homepage',
            name='video_content',
            field=wagtail.core.fields.StreamField([('rich_para_block', streams.core_blocks.VideoParaBlock())], blank=True, null=True),
        ),
    ]