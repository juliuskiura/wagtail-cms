# Generated by Django 3.2.9 on 2021-12-03 22:29

from django.db import migrations
import wagtail.core.fields
import wagtail.embeds.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20211203_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='video_link',
            field=wagtail.core.fields.StreamField([('embed', wagtail.embeds.blocks.EmbedBlock(max_height=400, max_width=800))], blank=True, null=True),
        ),
    ]