# Generated by Django 3.0.3 on 2020-02-10 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20200209_1408'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='external',
            options={'verbose_name': 'external'},
        ),
        migrations.AlterModelOptions(
            name='page',
            options={'verbose_name': 'page', 'verbose_name_plural': 'page'},
        ),
        migrations.AlterModelOptions(
            name='richtext',
            options={'verbose_name': 'rich text'},
        ),
    ]
