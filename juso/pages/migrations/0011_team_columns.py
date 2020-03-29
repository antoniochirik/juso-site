# Generated by Django 3.0.3 on 2020-03-24 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_remove_team_columns'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='columns',
            field=models.CharField(choices=[('two', '2'), ('three', '3'), ('four', '4'), ('five', '5')], default='three', max_length=10, verbose_name='columns'),
        ),
    ]