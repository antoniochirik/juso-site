# Generated by Django 3.0.5 on 2020-05-10 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0047_auto_20200510_1723'),
        ('blog', '0029_auto_20200510_1723'),
        ('events', '0029_auto_20200510_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='articleplugin',
            name='all_articles',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='pages.Page', verbose_name='page with all articles'),
        ),
        migrations.AddField(
            model_name='articleplugin',
            name='all_articles_override',
            field=models.CharField(blank=True, max_length=180, verbose_name='all article link text'),
        ),
        migrations.AlterField(
            model_name='articleplugin',
            name='articles',
            field=models.ManyToManyField(blank=True, related_name='events_articleplugin', to='blog.Article', verbose_name='Artikel'),
        ),
    ]
