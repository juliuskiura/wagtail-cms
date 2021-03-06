# Generated by Django 3.2.10 on 2021-12-14 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapplications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='formpage',
            name='from_address',
            field=models.CharField(blank=True, max_length=255, verbose_name='from address'),
        ),
        migrations.AddField(
            model_name='formpage',
            name='intro',
            field=models.TextField(default='Upload your resume'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formpage',
            name='subject',
            field=models.CharField(blank=True, max_length=255, verbose_name='subject'),
        ),
        migrations.AddField(
            model_name='formpage',
            name='thank_you_text',
            field=models.TextField(default='Thank you for your resume'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formpage',
            name='to_address',
            field=models.CharField(blank=True, help_text='Optional - form submissions will be emailed to these addresses. Separate multiple addresses by comma.', max_length=255, verbose_name='to address'),
        ),
        migrations.AlterField(
            model_name='formfield',
            name='field_type',
            field=models.CharField(choices=[('singleline', 'Single line text'), ('multiline', 'Multi-line text'), ('email', 'Email'), ('number', 'Number'), ('url', 'URL'), ('checkbox', 'Checkbox'), ('checkboxes', 'Checkboxes'), ('dropdown', 'Drop down'), ('multiselect', 'Multiple select'), ('radio', 'Radio buttons'), ('date', 'Date'), ('datetime', 'Date/time'), ('hidden', 'Hidden field'), ('document', 'Upload Document')], max_length=16, verbose_name='field type'),
        ),
    ]
