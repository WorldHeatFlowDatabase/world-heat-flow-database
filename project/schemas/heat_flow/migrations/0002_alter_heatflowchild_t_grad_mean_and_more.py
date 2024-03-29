# Generated by Django 4.2.11 on 2024-03-11 19:32

import django.core.validators
from django.db import migrations, models
import quantityfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('heat_flow', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heatflowchild',
            name='T_grad_mean',
            field=quantityfield.fields.QuantityField(base_units='K/km', blank=True, help_text='Mean temperature gradient measured for the heat-flow determination interval.', null=True, unit_choices=['K/km'], validators=[django.core.validators.MinValueValidator(-100000), django.core.validators.MaxValueValidator(100000)], verbose_name='Calculated or inferred temperature gradient'),
        ),
        migrations.AlterField(
            model_name='heatflowchild',
            name='T_number',
            field=models.PositiveSmallIntegerField(blank=True, help_text='Number of discrete temperature points (e.g. number of used BHT values, log values or thermistors used in probe sensing) confirming the mean temperature gradient [T_grad_mean_meas]. NOT the repetition of one measurement at a certain depth.', null=True, verbose_name='Number of temperature recordings'),
        ),
        migrations.AlterField(
            model_name='heatflowchild',
            name='corr_CONV_flag',
            field=models.CharField(choices=[('Present and corrected', 'Present and corrected'), ('Present and not corrected', 'Present and not corrected'), ('Present not significant', 'Present not significant'), ('not recognized', 'Not recognized'), ('unspecified', 'Unspecified')], default='unspecified', help_text='Specifies if convection effects with respect to the reported heat-flow value were present and if corrections were performed.', max_length=25, verbose_name='Flag convection processes (heat-flow correction)'),
        ),
        migrations.AlterField(
            model_name='heatflowchild',
            name='corr_E_flag',
            field=models.CharField(choices=[('Present and corrected', 'Present and corrected'), ('Present and not corrected', 'Present and not corrected'), ('Present not significant', 'Present not significant'), ('not recognized', 'Not recognized'), ('unspecified', 'Unspecified')], default='unspecified', help_text='Specifies if erosion effects with respect to the reported heat-flow value were present and if corrections were performed.', max_length=25, verbose_name='Flag erosion effect (heat-flow correction)'),
        ),
        migrations.AlterField(
            model_name='heatflowchild',
            name='corr_HR_flag',
            field=models.CharField(choices=[('Present and corrected', 'Present and corrected'), ('Present and not corrected', 'Present and not corrected'), ('Present not significant', 'Present not significant'), ('not recognized', 'Not recognized'), ('unspecified', 'Unspecified')], default='unspecified', help_text='Specifies if refraction effects, e.g., due to significant local conductivity contrasts, with respect to the reported heat-flow value were present and if corrections were performed. ', max_length=25, verbose_name='Flag heat refraction effect (heat-flow correction)'),
        ),
        migrations.AlterField(
            model_name='heatflowchild',
            name='corr_IS_flag',
            field=models.CharField(choices=[('Considered - p', 'Considered - p'), ('Considered - T', 'Considered - T'), ('Considered - pT', 'Considered - pT'), ('not Considered', 'Not considered'), ('unspecified', 'Unspecified')], default='unspecified', help_text='Specifies whether the in-situ pressure and temperature conditions were considered to the reported thermal conductivity value or not.', max_length=15, verbose_name='Flag in-situ thermal properties'),
        ),
        migrations.AlterField(
            model_name='heatflowchild',
            name='corr_PAL_flag',
            field=models.CharField(choices=[('Present and corrected', 'Present and corrected'), ('Present and not corrected', 'Present and not corrected'), ('Present not significant', 'Present not significant'), ('not recognized', 'Not recognized'), ('unspecified', 'Unspecified')], default='unspecified', help_text='Specifies if topographic effects with respect to the reported heat-flow value were present and if corrections were performed.', max_length=25, verbose_name='Flag paleoclimatic effect (heat-flow correction)'),
        ),
        migrations.AlterField(
            model_name='heatflowchild',
            name='corr_SUR_flag',
            field=models.CharField(choices=[('Present and corrected', 'Present and corrected'), ('Present and not corrected', 'Present and not corrected'), ('Present not significant', 'Present not significant'), ('not recognized', 'Not recognized'), ('unspecified', 'Unspecified')], default='unspecified', help_text='Specifies if climatic conditions (glaciation, post-industrial warming, etc.) with respect to the reported heat-flow value were present and if corrections were performed.', max_length=25, verbose_name='Flag in-situ thermal properties'),
        ),
        migrations.AlterField(
            model_name='heatflowchild',
            name='corr_TOPO_flag',
            field=models.CharField(choices=[('Present and corrected', 'Present and corrected'), ('Present and not corrected', 'Present and not corrected'), ('Present not significant', 'Present not significant'), ('not recognized', 'Not recognized'), ('unspecified', 'Unspecified')], default='unspecified', help_text='Specifies if topographic effects with respect to the reported heat-flow value were present and if corrections were performed.', max_length=25, verbose_name='Flag topographic effect (heat-flow correction)'),
        ),
        migrations.AlterField(
            model_name='heatflowchild',
            name='tc_strategy',
            field=models.CharField(blank=True, choices=[('Random or periodic depth sampling (number)', 'Random or periodic depth sampling (number)'), ('Characterize formation conductivities', 'Characterize formation conductivities'), ('Well log interpretation', 'Well log interpretation'), ('Computation from probe sensing', 'Computation from probe sensing'), ('Other', 'Other'), ('unspecified', 'Unspecified')], help_text='Strategy that was employed to estimate the thermal conductivity over the vertical interval of heat-flow determination.', max_length=255, null=True, verbose_name='Thermal conductivity averaging methodology'),
        ),
    ]
