# Generated by Django 3.0.3 on 2020-03-24 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_auto_20200324_2039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='divider',
            name='header',
        ),
    ]
