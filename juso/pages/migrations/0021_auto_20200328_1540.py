# Generated by Django 3.0.3 on 2020-03-28 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0003_auto_20200302_1952'),
        ('blog', '0011_auto_20200328_1540'),
        ('pages', '0020_auto_20200328_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventplugin',
            name='template_key',
            field=models.CharField(choices=[('events/plugins/default.html', 'default')], default='events/plugins/default.html', max_length=100),
        ),
        migrations.CreateModel(
            name='ArticlePlugin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(choices=[('de', 'German'), ('fr', 'French'), ('it', 'Italian')], default='de', max_length=10, verbose_name='language')),
                ('count', models.IntegerField(default=3, verbose_name='count')),
                ('template_key', models.CharField(choices=[('blog/plugins/default.html', 'default')], default='blog/plugins/default.html', max_length=100)),
                ('region', models.CharField(max_length=255)),
                ('ordering', models.IntegerField(default=0)),
                ('articles', models.ManyToManyField(blank=True, related_name='_articleplugin_articles_+', related_query_name='+', to='blog.Article', verbose_name='articles')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='sections.Category', verbose_name='category')),
                ('namespace', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='blog.NameSpace', verbose_name='namespace')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pages_articleplugin_set', to='pages.Page')),
                ('sections', models.ManyToManyField(blank=True, related_name='_articleplugin_sections_+', related_query_name='+', to='sections.Section')),
                ('translations', models.ManyToManyField(blank=True, related_name='_articleplugin_translations_+', to='pages.ArticlePlugin')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
