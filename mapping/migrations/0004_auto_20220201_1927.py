# Generated by Django 3.2.11 on 2022-02-01 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0003_auto_20220201_1818'),
    ]

    operations = [
        migrations.CreateModel(
            name='GISPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package', models.FileField(blank=True, null=True, upload_to='', verbose_name='GIS Shape file')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'GIS package',
                'verbose_name_plural': 'GIS packages',
                'db_table': 'gis_package',
            },
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ['name'], 'verbose_name': 'country', 'verbose_name_plural': 'countries'},
        ),
        migrations.RemoveField(
            model_name='continent',
            name='shape_area',
        ),
        migrations.RemoveField(
            model_name='continent',
            name='shape_leng',
        ),
        migrations.RemoveField(
            model_name='continent',
            name='sqkm',
        ),
        migrations.RemoveField(
            model_name='continent',
            name='sqmi',
        ),
        migrations.RemoveField(
            model_name='province',
            name='area_km2',
        ),
        migrations.RemoveField(
            model_name='province',
            name='comments',
        ),
    ]
