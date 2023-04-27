# Generated by Django 3.2.18 on 2023-03-23 16:16

import controlled_vocabulary.models
from django.db import migrations, models
import django.db.models.deletion
import quantityfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('controlled_vocabulary', '0005_auto_20230323_1534'),
        ('ghfdb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interval',
            name='T_correction_bottom',
        ),
        migrations.RemoveField(
            model_name='interval',
            name='T_correction_top',
        ),
        migrations.RemoveField(
            model_name='interval',
            name='T_count',
        ),
        migrations.RemoveField(
            model_name='interval',
            name='T_grad_mean',
        ),
        migrations.RemoveField(
            model_name='interval',
            name='T_grad_mean_cor',
        ),
        migrations.RemoveField(
            model_name='interval',
            name='T_grad_uncertainty',
        ),
        migrations.RemoveField(
            model_name='interval',
            name='T_grad_uncertainty_cor',
        ),
        migrations.RemoveField(
            model_name='interval',
            name='T_method_bottom',
        ),
        migrations.RemoveField(
            model_name='interval',
            name='T_method_top',
        ),
        migrations.RemoveField(
            model_name='interval',
            name='T_shutin_bottom',
        ),
        migrations.RemoveField(
            model_name='interval',
            name='T_shutin_top',
        ),
        migrations.CreateModel(
            name='Temperature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grad_mean', quantityfield.fields.QuantityField(base_units='K/km', blank=True, help_text='measured temperature gradient for the heat-flow determination interval.', null=True, unit_choices=['K/km'], verbose_name='measured gradient')),
                ('grad_uncertainty', quantityfield.fields.QuantityField(base_units='K/km', blank=True, help_text='uncertainty (standard deviation) of the measured temperature gradient estimated by error propagation from uncertainty in the top and bottom interval temperatures.', null=True, unit_choices=['K/km'], verbose_name='uncertainty')),
                ('grad_mean_cor', quantityfield.fields.QuantityField(base_units='K/km', blank=True, help_text='temperature gradient corrected for borehole and environmental effects. Correction method should be recorded in the relevant field.', null=True, unit_choices=['K/km'], verbose_name='corrected gradient')),
                ('grad_uncertainty_cor', quantityfield.fields.QuantityField(base_units='K/km', blank=True, help_text='uncertainty (standard deviation) of the corrected temperature gradient estimated by error propagation from uncertainty of the measured gradient and the applied correction approaches.', null=True, unit_choices=['K/km'], verbose_name='uncertainty')),
                ('shutin_top', quantityfield.fields.PositiveIntegerQuantityField(base_units='hour', blank=True, help_text='Time of measurement at the interval top in relation to the end of drilling/end of mud circulation. Positive values are measured after the drilling, 0 represents temperatures measured during the drilling.', null=True, unit_choices=['hour'], verbose_name='Shut-in time (top)')),
                ('shutin_bottom', quantityfield.fields.PositiveIntegerQuantityField(base_units='hour', blank=True, help_text='Time of measurement at the interval bottom in relation to the end of drilling/end of mud circulation. Positive values are measured after the drilling, 0 represents temperatures measured during the drilling.', null=True, unit_choices=['hour'], verbose_name='Shut-in time (bottom; hrs)')),
                ('count', models.PositiveSmallIntegerField(blank=True, help_text='Number of discrete temperature points (e.g. number of used BHT values, log values or thermistors used in probe sensing) confirming the mean temperature gradient. Not the repetition of one measurement at a certain depth.', null=True, verbose_name='number of temperature recordings')),
                ('correction_bottom', controlled_vocabulary.models.ControlledTermField(blank=True, help_text='Approach used at the bottom of the heat flow interval to correct the measured temperature for drilling perturbations.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='controlled_vocabulary.controlledterm', verbose_name='correction method (bottom)', vocabularies='T_correction_method')),
                ('correction_top', controlled_vocabulary.models.ControlledTermField(blank=True, help_text='Approach used at the top of the heat flow interval to correct the measured temperature for drilling perturbations.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='controlled_vocabulary.controlledterm', verbose_name='correction method (top)', vocabularies='T_correction_method')),
                ('interval', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='temp', to='ghfdb.interval')),
                ('method_bottom', controlled_vocabulary.models.ControlledTermField(blank=True, help_text='Method used to determine temperature at the bottom of the heat flow interval.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='controlled_vocabulary.controlledterm', verbose_name='temperature method (bottom)', vocabularies='T_method')),
                ('method_top', controlled_vocabulary.models.ControlledTermField(blank=True, help_text='Method used to determine temperature at the top of the heat flow interval.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='controlled_vocabulary.controlledterm', verbose_name='temperature method (top)', vocabularies='T_method')),
            ],
            options={
                'verbose_name': 'Temperature',
                'verbose_name_plural': 'Temperature Data',
            },
        ),
    ]