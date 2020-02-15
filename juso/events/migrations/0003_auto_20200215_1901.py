# Generated by Django 3.0.3 on 2020-02-15 19:01

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sections', '0001_initial'),
        ('events', '0002_auto_20200215_1901'),
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sections.Category', verbose_name='category'),
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.Location', verbose_name='location'),
        ),
        migrations.AddField(
            model_name='event',
            name='namespace',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='events.NameSpace', verbose_name='namespace'),
        ),
        migrations.AddField(
            model_name='event',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sections.Section', verbose_name='section'),
        ),
        migrations.AddField(
            model_name='event',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='download',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events_download_set', to='events.Event'),
        ),
        migrations.AlterUniqueTogether(
            name='event',
            unique_together={('slug', 'section')},
        ),
    ]
