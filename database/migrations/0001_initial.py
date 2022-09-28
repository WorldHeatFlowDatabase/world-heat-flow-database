# Generated by Django 3.2.15 on 2022-09-27 16:05

import core.fields
import database.fields
import django.contrib.gis.db.models.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_ckeditor_5.fields
import meta.models
import shortuuid.django_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('global_tectonics', '0004_auto_20220914_0201'),
        ('mapping', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255, unique=True)),
                ('depth', models.PositiveIntegerField()),
                ('numchild', models.PositiveIntegerField(default=0)),
                ('code', models.CharField(max_length=64, verbose_name='code')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('description', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'Field Choice',
                'verbose_name_plural': 'Field Choice',
            },
        ),
        migrations.CreateModel(
            name='Interval',
            fields=[
                ('id', shortuuid.django_fields.ShortUUIDField(alphabet='23456789ABCDEFGHJKLMNPQRSTUVWXYZ', length=8, max_length=15, prefix='GHFI-', primary_key=True, serialize=False)),
                ('historic_id', models.PositiveIntegerField(blank=True, help_text='This is the numeric identifier used in old forms of the GHFDB to identify measurements', null=True, verbose_name='Historic ID')),
                ('qc', models.FloatField(help_text='heat flow value', verbose_name='heat flow')),
                ('qc_unc', core.fields.RangeField(blank=True, help_text='uncertainty standard deviation of the reported heat-flow value as estimated by an error propagation from uncertainty in thermal conductivity and temperature gradient (corrected preferred over measured gradient).', null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='uncertainty')),
                ('q_top', core.fields.RangeField(blank=True, help_text='Describes the true vertical depth of the top end of the heat-flow determination interval relative to the land surface/ocean bottom.', null=True, validators=[django.core.validators.MaxValueValidator(12500)], verbose_name='interval top (m)')),
                ('q_bot', core.fields.RangeField(blank=True, help_text='Describes the true vertical depth of the bottom end of the heat-flow determination interval relative to the land surface/ocean bottom.', null=True, validators=[django.core.validators.MaxValueValidator(12500), django.core.validators.MinValueValidator(0)], verbose_name='interval bottom (m)')),
                ('hf_pen', core.fields.RangeField(blank=True, help_text='Depth of penetration of marine probe into the sediment.', null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], verbose_name='penetration depth (m)')),
                ('hf_probeL', core.fields.RangeField(blank=True, help_text='length of the marine probe.', null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], verbose_name='probe length (m)')),
                ('T_tilt', core.fields.RangeField(blank=True, help_text='Tilt of the marine probe.', null=True, validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(0)], verbose_name='tilt (deg)')),
                ('q_acq', models.DateField(blank=True, help_text='Year of acquisition of the heat-flow data (may differ from publication year)', null=True, verbose_name='date of acquisition (YYYY-MM)')),
                ('childcomp', models.BooleanField(blank=True, default=None, help_text='Specifies whether the child entry is used for computation of representative location heat flow values at the parent level or not.', null=True, verbose_name='Is relevant child?')),
                ('T_grad_mean_meas', models.FloatField(blank=True, help_text='measured temperature gradient for the heat-flow determination interval.', null=True, verbose_name='measured gradient (K/km)')),
                ('T_grad_unc_meas', models.FloatField(blank=True, help_text='uncertainty (standard deviation) of the measured temperature gradient estimated by error propagation from uncertainty in the top and bottom interval temperatures.', null=True, verbose_name='uncertainty (K/km)')),
                ('T_grad_mean_cor', models.FloatField(blank=True, help_text='temperature gradient corrected for borehole and environmental effects. Correction method should be recorded in the relevant field.', null=True, verbose_name='corrected gradient (K/km)')),
                ('T_grad_unc_cor', models.FloatField(blank=True, help_text='uncertainty (standard deviation) of the corrected temperature gradient estimated by error propagation from uncertainty of the measured gradient and the applied correction approaches.', null=True, verbose_name='uncertainty (K/km)')),
                ('T_shutin_top', models.PositiveSmallIntegerField(blank=True, help_text='Time of measurement at the interval top in relation to the end of drilling/end of mud circulation. Positive values are measured after the drilling, 0 represents temperatures measured during the drilling.', null=True, verbose_name='Shut-in time (top; hrs)')),
                ('T_shutin_bot', models.PositiveSmallIntegerField(blank=True, help_text='Time of measurement at the interval bottom in relation to the end of drilling/end of mud circulation. Positive values are measured after the drilling, 0 represents temperatures measured during the drilling.', null=True, verbose_name='Shut-in time (bottom; hrs)')),
                ('T_numb', models.PositiveSmallIntegerField(blank=True, help_text='Number of discrete temperature points (e.g. number of used BHT values, log values or thermistors used in probe sensing) confirming the mean temperature gradient. Not the repetition of one measurement at a certain depth.', null=True, verbose_name='number of temperature recordings')),
                ('tc_mean', core.fields.RangeField(blank=True, help_text='Mean conductivity in the vertical direction representative for the heat-flow determination interval. Value should reflect true in-situ conditions for the interval.', null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], verbose_name='Mean conductivity (W/mK)')),
                ('tc_unc', core.fields.RangeField(blank=True, help_text='Uncertainty of the mean thermal conductivity given as one-sigma standard deviation.', null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], verbose_name='uncertainty')),
                ('tc_meth', models.CharField(blank=True, help_text='Method used to determine the mean thermal conductivity over the given interval', max_length=100, null=True, verbose_name='method')),
                ('tc_satur', models.CharField(blank=True, help_text='Saturation state of the rock sample studied for thermal conductivity', max_length=100, null=True, verbose_name='saturation state')),
                ('tc_pTfunc', models.CharField(blank=True, help_text='Technique or approach used to correct the measured thermal conductivity towards in-situ pT conditions', max_length=255, null=True, verbose_name='assumed pT function')),
                ('tc_strategy', models.CharField(blank=True, help_text='Strategy employed to estimate thermal conductivity over the given interval', max_length=255, null=True, verbose_name='averaging methodoloy')),
                ('tc_numb', models.PositiveSmallIntegerField(blank=True, help_text='Number of discrete temperature points (e.g. number of used BHT values, log values or thermistors used in probe sensing) confirming the mean temperature gradient. Not the repetition of one measurement at a certain depth.', null=True, verbose_name='number of temperature recordings')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='last modified')),
            ],
            options={
                'verbose_name': 'Heat Flow',
                'verbose_name_plural': 'Heat Flow',
                'db_table': 'heat_flow_interval',
                'ordering': ['date_added'],
                'abstract': False,
                'default_related_name': 'intervals',
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('geom', django.contrib.gis.db.models.fields.PointField(blank=True, srid=4326)),
                ('id', shortuuid.django_fields.ShortUUIDField(alphabet='23456789ABCDEFGHJKLMNPQRSTUVWXYZ', length=10, max_length=15, prefix='GHFS-', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Specification of the (local) name of the related heat-flow site or the related survey.', max_length=255, null=True, verbose_name='name')),
                ('lat', models.DecimalField(db_index=True, decimal_places=5, help_text='Latitude in decimal degrees', max_digits=7, validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(-90)], verbose_name='latitude')),
                ('lng', models.DecimalField(db_index=True, decimal_places=5, help_text='Longitude in decimal degrees', max_digits=8, validators=[django.core.validators.MaxValueValidator(180), django.core.validators.MinValueValidator(-180)], verbose_name='longitude')),
                ('elevation', core.fields.RangeField(blank=True, help_text='site elevation with reference to mean sea level (m)', null=True, validators=[django.core.validators.MaxValueValidator(9000), django.core.validators.MinValueValidator(-12000)], verbose_name='elevation (m)')),
                ('q', models.FloatField(help_text='site heat flow value', verbose_name='heat flow')),
                ('q_unc', core.fields.RangeField(blank=True, help_text='uncertainty standard deviation of the reported heat-flow value as estimated by an error propagation from uncertainty in thermal conductivity and temperature gradient (corrected preferred over measured gradient).', null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='heat flow uncertainty')),
                ('q_acq', models.DateField(help_text='Year of acquisition of the heat-flow data in the form "YYYY-MM" (may differ from publication year)', null=True, verbose_name='date acquired')),
                ('wat_temp', models.FloatField(blank=True, help_text='Seafloor temperature where heat-flow measurements were taken.', null=True, verbose_name='bottom water temperature (°C)')),
                ('q_comment', models.TextField(blank=True, help_text='General comments regarding the heat flow site/measurement', null=True, verbose_name='general comments')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='last modified')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('continent', models.ForeignKey(blank=True, help_text='Continent land boundaries', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sites', to='mapping.continent', verbose_name='continent')),
                ('country', models.ForeignKey(blank=True, help_text='Country land boundaries', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sites', to='mapping.country', verbose_name='country')),
                ('env', database.fields.ChoicesOneToOne(blank=True, help_text='Describes the general geographical setting of the heat-flow site (not the applied methodology).', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='database.choice', verbose_name='basic geographical environment')),
                ('expl', database.fields.ChoicesOneToOne(blank=True, help_text='Main purpose of the original excavation providing access for the temperature sensors.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='database.choice', verbose_name='exploration purpose')),
                ('method', database.fields.ChoicesOneToOne(blank=True, help_text='Specification of the general means by which the rock was accessed by temperature sensors for the respective data entry.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='database.choice', verbose_name='exploration method')),
                ('ocean', models.ForeignKey(blank=True, help_text='Global oceans and seas', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sites', to='mapping.ocean', verbose_name='ocean')),
                ('plate', models.ForeignKey(blank=True, help_text='tectonic plate', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sites', to='global_tectonics.plate', verbose_name='plate')),
                ('political', models.ForeignKey(blank=True, help_text='Countries inclusive of exclusive marine economic zones', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sites', to='mapping.political', verbose_name='political region')),
                ('province', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sites', to='global_tectonics.province', verbose_name='geological province')),
            ],
            options={
                'verbose_name': 'Site',
                'verbose_name_plural': 'Sites',
                'db_table': 'site',
                'ordering': ['-date_added'],
                'abstract': False,
                'default_related_name': 'sites',
            },
            bases=(meta.models.ModelMeta, models.Model),
        ),
    ]