# Generated by Django 3.2.9 on 2021-12-11 12:20

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_auto_20211211_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='cta_button_1',
            field=wagtail.core.fields.StreamField([('button_text', wagtail.core.blocks.CharBlock(max_length=50, required=False)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.core.blocks.URLBlock(required=False))]),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='cta_button_2',
            field=wagtail.core.fields.StreamField([('button_text', wagtail.core.blocks.CharBlock(max_length=50, required=False)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.core.blocks.URLBlock(required=False))]),
        ),
        migrations.CreateModel(
            name='HomePageArticles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('article_container', wagtail.core.fields.StreamField([('article_content', wagtail.core.blocks.PageChooserBlock(required=False))])),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_articles', to='home.homepage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]