# Generated by Django 3.2.10 on 2021-12-13 11:16

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0009_remove_articledetails_article_category'),
        ('wagtailcore', '0066_collection_management_permissions'),
        ('wagtailimages', '0023_add_choose_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('banner_intro_small', models.CharField(max_length=50, null=True)),
                ('banner_header', models.CharField(max_length=50, null=True)),
                ('contact_section_heading', models.CharField(max_length=50, null=True)),
                ('contact_section_para', models.TextField(null=True)),
                ('video_link', wagtail.core.fields.StreamField([('embed', wagtail.embeds.blocks.EmbedBlock(max_height=400, max_width=800))], blank=True, null=True)),
                ('first_article_link', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='firstarticle', to='blog.articledetails')),
                ('second_article_link', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='secondarticle', to='blog.articledetails')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='HomePageCarousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('carousel_title', models.CharField(max_length=50, null=True)),
                ('carousel_content', wagtail.core.fields.StreamField([('carousel_content', wagtail.core.blocks.RichTextBlock())])),
                ('carousel_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='carousel', to='home.homepage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
