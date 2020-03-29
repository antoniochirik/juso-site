# Generated by Django 3.0.3 on 2020-03-02 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0002_category_translations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='translations',
            field=models.ManyToManyField(blank=True, related_name='_category_translations_+', to='sections.Category'),
        ),
    ]