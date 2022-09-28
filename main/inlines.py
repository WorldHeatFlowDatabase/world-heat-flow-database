from main import models
from django.contrib import admin

class Interval(admin.TabularInline):
    model = models.Interval
    fields = ['heat_flow_corrected','heat_flow_corrected_uncertainty','heat_flow_uncorrected','heat_flow_uncorrected_uncertainty']
    extra=0

class Conductivity(admin.TabularInline):
    model = models.Conductivity
    fields = ['value','uncertainty','method','number_of_measurements',]

class HeatProduction(admin.TabularInline):
    model = models.HeatProduction
    fields = ['value','uncertainty','method','number_of_measurements',]

class Corrections(admin.StackedInline):
    model = models.Correction
    fields = [
        ('climate_flag','climate'),
        ('topographic_flag','topographic'),
        ('sed_erosion_flag','sed_erosion'),
        ('bwv_flag','bwv'),
        ('refraction_flag','refraction'),
        ('fluid_flag','fluid'),
        ('compaction_flag','compaction'),
        ('other_flag','other_type','other'),       
        ]

    classes = ['collapse']
