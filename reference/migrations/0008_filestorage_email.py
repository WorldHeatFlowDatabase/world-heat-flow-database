# Generated by Django 2.2.1 on 2019-09-18 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0007_auto_20190917_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='filestorage',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
