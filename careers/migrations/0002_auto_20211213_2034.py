# Generated by Django 3.2.10 on 2021-12-13 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('careers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobCategory',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('category_description', models.TextField()),
            ],
            options={
                'verbose_name': 'Job Category',
                'verbose_name_plural': 'Job Categories',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterField(
            model_name='joblist',
            name='jobs_per_page',
            field=models.IntegerField(),
        ),
    ]
