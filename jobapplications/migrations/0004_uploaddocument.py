# Generated by Django 3.2.10 on 2021-12-14 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jobapplications', '0003_auto_20211214_1119'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant_email', models.EmailField(max_length=50)),
                ('document', models.FileField(upload_to='careers/')),
            ],
        ),
    ]
