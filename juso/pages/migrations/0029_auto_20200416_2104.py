# Generated by Django 3.0.3 on 2020-04-16 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0028_glossaryrichtext_glossary_text'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='formplugin',
            options={'verbose_name': 'form'},
        ),
        migrations.AlterField(
            model_name='page',
            name='application',
            field=models.CharField(blank=True, choices=[('blog', 'blog'), ('people', 'people'), ('events', 'events'), ('categories', 'categories'), ('forms', 'forms'), ('glossary', 'glossary')], max_length=20, verbose_name='application'),
        ),
    ]