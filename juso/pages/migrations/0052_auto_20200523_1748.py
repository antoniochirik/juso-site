# Generated by Django 3.0.5 on 2020-05-23 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0019_auto_20200523_1748'),
        ('events', '0035_auto_20200523_1748'),
        ('people', '0011_auto_20200508_2342'),
        ('glossary', '0006_auto_20200523_1748'),
        ('sections', '0009_auto_20200507_1758'),
        ('blog', '0034_auto_20200523_1748'),
        ('pages', '0051_auto_20200510_1938'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articleplugin',
            options={'verbose_name': 'article plugin', 'verbose_name_plural': 'article plugins'},
        ),
        migrations.AlterModelOptions(
            name='download',
            options={'verbose_name': 'download', 'verbose_name_plural': 'downloads'},
        ),
        migrations.AlterModelOptions(
            name='eventplugin',
            options={'verbose_name': 'event plugin', 'verbose_name_plural': 'event plugins'},
        ),
        migrations.AlterModelOptions(
            name='page',
            options={'verbose_name': 'page', 'verbose_name_plural': 'page'},
        ),
        migrations.AlterField(
            model_name='articleplugin',
            name='articles',
            field=models.ManyToManyField(blank=True, related_name='pages_articleplugin', to='blog.Article', verbose_name='articles'),
        ),
        migrations.AlterField(
            model_name='articleplugin',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='sections.Category', verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='articleplugin',
            name='count',
            field=models.IntegerField(default=3, verbose_name='count'),
        ),
        migrations.AlterField(
            model_name='articleplugin',
            name='namespace',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='blog.NameSpace', verbose_name='namespace'),
        ),
        migrations.AlterField(
            model_name='articleplugin',
            name='title',
            field=models.CharField(blank=True, max_length=180, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='button',
            name='align',
            field=models.CharField(blank=True, choices=[('', 'default'), ('center', 'center'), ('right', 'right'), ('block', 'block')], max_length=30, verbose_name='alignment'),
        ),
        migrations.AlterField(
            model_name='button',
            name='style',
            field=models.CharField(blank=True, choices=[('', 'none'), ('secondary', 'secondary')], default='', max_length=20, verbose_name='style'),
        ),
        migrations.AlterField(
            model_name='button',
            name='target',
            field=models.CharField(max_length=800, verbose_name='target'),
        ),
        migrations.AlterField(
            model_name='button',
            name='text',
            field=models.CharField(blank=True, max_length=240, verbose_name='text'),
        ),
        migrations.AlterField(
            model_name='download',
            name='document',
            field=models.FileField(upload_to='downloads/', verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='download',
            name='download_text',
            field=models.CharField(max_length=200, verbose_name='download text'),
        ),
        migrations.AlterField(
            model_name='download',
            name='link_classes',
            field=models.CharField(blank=True, max_length=200, verbose_name='link classes (css)'),
        ),
        migrations.AlterField(
            model_name='eventplugin',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', related_query_name='+', to='sections.Category', verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='eventplugin',
            name='count',
            field=models.IntegerField(default=3, verbose_name='count'),
        ),
        migrations.AlterField(
            model_name='eventplugin',
            name='events',
            field=models.ManyToManyField(blank=True, related_name='_eventplugin_events_+', related_query_name='+', to='events.Event', verbose_name='events'),
        ),
        migrations.AlterField(
            model_name='eventplugin',
            name='namespace',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', related_query_name='+', to='events.NameSpace', verbose_name='namespace'),
        ),
        migrations.AlterField(
            model_name='eventplugin',
            name='title',
            field=models.CharField(blank=True, max_length=180, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='formplugin',
            name='form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pages_formplugin', to='forms.Form', verbose_name='form'),
        ),
        migrations.AlterField(
            model_name='glossaryrichtext',
            name='entries',
            field=models.ManyToManyField(related_name='pages_glossaryrichtext_related', related_query_name='pages_glossaryrichtexts', to='glossary.Entry', verbose_name='entries'),
        ),
        migrations.AlterField(
            model_name='team',
            name='columns',
            field=models.CharField(choices=[('two', '2'), ('three', '3'), ('four', '4'), ('five', '5')], default='three', max_length=10, verbose_name='columns'),
        ),
        migrations.AlterField(
            model_name='team',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='people.Team', verbose_name='team'),
        ),
    ]
