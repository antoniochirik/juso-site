# Generated by Django 3.0.3 on 2020-04-13 10:24

import feincms3.cleanse
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0004_auto_20200412_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='formfield',
            name='size',
            field=models.TextField(choices=[('one', 'one'), ('two', 'two'), ('three', 'three'), ('four', 'four'), ('five', 'five'), ('six', 'six'), ('seven', 'seven'), ('eight', 'eight'), ('nine', 'nine'), ('ten', 'ten'), ('eleven', 'eleven'), ('twelve', 'twelve'), ('thirteen', 'thirteen'), ('fourteen', 'fourteen'), ('fifteen', 'fifteen'), ('sixteen', 'sixteen'), ('seventeen', 'seventeen')], default='eighteen', verbose_name='size'),
        ),
        migrations.AlterField(
            model_name='form',
            name='success_message',
            field=feincms3.cleanse.CleansedRichTextField(blank=True, verbose_name='success message'),
        ),
    ]