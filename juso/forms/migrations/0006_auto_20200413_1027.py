# Generated by Django 3.0.3 on 2020-04-13 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0005_auto_20200413_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formfield',
            name='size',
            field=models.TextField(choices=[('one', 'one'), ('two', 'two'), ('three', 'three'), ('four', 'four'), ('five', 'five'), ('six', 'six'), ('seven', 'seven'), ('eight', 'eight'), ('nine', 'nine'), ('ten', 'ten'), ('eleven', 'eleven'), ('twelve', 'twelve'), ('thirteen', 'thirteen'), ('fourteen', 'fourteen'), ('fifteen', 'fifteen'), ('sixteen', 'sixteen'), ('seventeen', 'seventeen'), ('eighteen', 'eighteen')], default='eighteen', verbose_name='size'),
        ),
    ]
