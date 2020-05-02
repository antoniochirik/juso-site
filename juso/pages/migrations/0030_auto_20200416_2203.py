# Generated by Django 3.0.3 on 2020-04-16 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glossary', '0003_auto_20200416_2112'),
        ('pages', '0029_auto_20200416_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='glossaryrichtext',
            name='entries',
            field=models.ManyToManyField(related_name='pages_glossaryrichtext_related', related_query_name='pages_glossaryrichtexts', to='glossary.Entry', verbose_name='entries'),
        ),
    ]