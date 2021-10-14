# Generated by Django 3.1.3 on 2021-07-07 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('editorial', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Heading',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='editorial_heading', serialize=False, to='cms.cmsplugin')),
                ('heading', models.CharField(max_length=256)),
                ('sub_heading', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
