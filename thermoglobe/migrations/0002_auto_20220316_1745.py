# Generated by Django 3.2.12 on 2022-03-16 07:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thermoglobe', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='site',
            options={'default_related_name': 'sites', 'ordering': ['-date_added']},
        ),
        migrations.AlterField(
            model_name='historicalsite',
            name='cruise',
            field=models.CharField(blank=True, help_text='For oceanic measurements - the name of the cruise on which the measurements were taken.', max_length=150, null=True, verbose_name='cruise name'),
        ),
        migrations.AlterField(
            model_name='historicalsite',
            name='crustal_thickness',
            field=models.FloatField(blank=True, help_text='Calculated crustal thickness at the site.', null=True, verbose_name='crustal thickness'),
        ),
        migrations.AlterField(
            model_name='historicalsite',
            name='date_added',
            field=models.DateTimeField(blank=True, editable=False, verbose_name='date added'),
        ),
        migrations.AlterField(
            model_name='historicalsite',
            name='elevation',
            field=models.FloatField(blank=True, help_text='Site elevation', null=True, verbose_name='elevation (m)'),
        ),
        migrations.AlterField(
            model_name='historicalsite',
            name='outcrop_distance',
            field=models.FloatField(blank=True, help_text='Distance in Km to the nearest outcrop.', null=True, verbose_name='outcrop distance'),
        ),
        migrations.AlterField(
            model_name='historicalsite',
            name='seamount_distance',
            field=models.FloatField(blank=True, help_text='Distance in Km to the nearest seamount.', null=True, verbose_name='seamount distance'),
        ),
        migrations.AlterField(
            model_name='historicalsite',
            name='sediment_thickness',
            field=models.FloatField(blank=True, help_text='Sediment thickness at the site.', null=True, verbose_name='sediment thickness'),
        ),
        migrations.AlterField(
            model_name='historicalsite',
            name='sediment_thickness_type',
            field=models.CharField(blank=True, help_text='How sediment thickness was determined.', max_length=250, null=True, verbose_name='sediment thickness'),
        ),
        migrations.AlterField(
            model_name='historicalsite',
            name='well_depth',
            field=models.FloatField(blank=True, help_text='Total depth of the hole in metres.', null=True, validators=[django.core.validators.MaxValueValidator(12500), django.core.validators.MinValueValidator(0)], verbose_name='well depth (m)'),
        ),
        migrations.AlterField(
            model_name='interval',
            name='average_conductivity',
            field=models.FloatField(blank=True, help_text='Reported thermal conductivity to accompany the heat flow estimate.', null=True, verbose_name='conductivity'),
        ),
        migrations.AlterField(
            model_name='site',
            name='cruise',
            field=models.CharField(blank=True, help_text='For oceanic measurements - the name of the cruise on which the measurements were taken.', max_length=150, null=True, verbose_name='cruise name'),
        ),
        migrations.AlterField(
            model_name='site',
            name='crustal_thickness',
            field=models.FloatField(blank=True, help_text='Calculated crustal thickness at the site.', null=True, verbose_name='crustal thickness'),
        ),
        migrations.AlterField(
            model_name='site',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date added'),
        ),
        migrations.AlterField(
            model_name='site',
            name='elevation',
            field=models.FloatField(blank=True, help_text='Site elevation', null=True, verbose_name='elevation (m)'),
        ),
        migrations.AlterField(
            model_name='site',
            name='outcrop_distance',
            field=models.FloatField(blank=True, help_text='Distance in Km to the nearest outcrop.', null=True, verbose_name='outcrop distance'),
        ),
        migrations.AlterField(
            model_name='site',
            name='seamount_distance',
            field=models.FloatField(blank=True, help_text='Distance in Km to the nearest seamount.', null=True, verbose_name='seamount distance'),
        ),
        migrations.AlterField(
            model_name='site',
            name='sediment_thickness',
            field=models.FloatField(blank=True, help_text='Sediment thickness at the site.', null=True, verbose_name='sediment thickness'),
        ),
        migrations.AlterField(
            model_name='site',
            name='sediment_thickness_type',
            field=models.CharField(blank=True, help_text='How sediment thickness was determined.', max_length=250, null=True, verbose_name='sediment thickness'),
        ),
        migrations.AlterField(
            model_name='site',
            name='well_depth',
            field=models.FloatField(blank=True, help_text='Total depth of the hole in metres.', null=True, validators=[django.core.validators.MaxValueValidator(12500), django.core.validators.MinValueValidator(0)], verbose_name='well depth (m)'),
        ),
    ]
