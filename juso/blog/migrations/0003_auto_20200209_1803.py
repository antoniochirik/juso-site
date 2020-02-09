# Generated by Django 3.0.3 on 2020-02-09 18:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0002_auto_20200209_1421'),
        ('blog', '0002_auto_20200209_1408'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'get_latest_by': 'publication_date', 'ordering': ['-publication_date']},
        ),
        migrations.AddField(
            model_name='article',
            name='publication_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='publication date'),
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, to='sections.Tag'),
        ),
    ]
