# Generated by Django 3.1.3 on 2020-12-15 06:02

from django.db import migrations, models
import thermoglobe.models.publications


class Migration(migrations.Migration):

    dependencies = [
        ('thermoglobe', '0038_delete_siteproxy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalpublication',
            name='uploaded_by',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='uploaded_by',
        ),
        migrations.AddField(
            model_name='historicalpublication',
            name='file',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='file'),
        ),
        migrations.AddField(
            model_name='publication',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=thermoglobe.models.publications.pdf_path, verbose_name='file'),
        ),
    ]
