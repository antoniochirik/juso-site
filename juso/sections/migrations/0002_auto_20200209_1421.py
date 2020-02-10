# Generated by Django 3.0.3 on 2020-02-09 14:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feincms3_sites', '0004_site_is_active'),
        ('sections', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='site',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='section', to='feincms3_sites.Site', verbose_name='section'),
        ),
    ]
