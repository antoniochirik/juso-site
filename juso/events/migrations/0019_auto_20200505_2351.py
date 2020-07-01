# Generated by Django 3.0.5 on 2020-05-05 21:51

import django.db.models.deletion
import django.utils.timezone
import imagefield.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("people", "0009_merge_20200324_2216"),
        ("sections", "0007_auto_20200502_2048"),
        ("blog", "0018_auto_20200505_2351"),
        ("forms", "0013_auto_20200429_1939"),
        ("events", "0018_auto_20200429_1943"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="download",
            options={"verbose_name": "Download", "verbose_name_plural": "Downloads"},
        ),
        migrations.AlterModelOptions(
            name="event",
            options={
                "ordering": ["start_date"],
                "verbose_name": "Event",
                "verbose_name_plural": "Events",
            },
        ),
        migrations.AlterModelOptions(
            name="location",
            options={
                "ordering": ["name"],
                "verbose_name": "Ort",
                "verbose_name_plural": "Orte",
            },
        ),
        migrations.AlterField(
            model_name="articleplugin",
            name="articles",
            field=models.ManyToManyField(
                blank=True,
                related_name="_articleplugin_articles_+",
                related_query_name="+",
                to="blog.Article",
                verbose_name="Artikel",
            ),
        ),
        migrations.AlterField(
            model_name="articleplugin",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="sections.Category",
                verbose_name="Kategorie",
            ),
        ),
        migrations.AlterField(
            model_name="articleplugin",
            name="count",
            field=models.IntegerField(default=3, verbose_name="Anzahl"),
        ),
        migrations.AlterField(
            model_name="articleplugin",
            name="namespace",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="blog.NameSpace",
                verbose_name="Namensraum",
            ),
        ),
        migrations.AlterField(
            model_name="button",
            name="style",
            field=models.CharField(
                blank=True,
                choices=[("", "keine"), ("secondary", "sekundär")],
                default="",
                max_length=20,
                verbose_name="Styl",
            ),
        ),
        migrations.AlterField(
            model_name="download",
            name="download_text",
            field=models.CharField(max_length=200, verbose_name="Download Text"),
        ),
        migrations.AlterField(
            model_name="download",
            name="link_classes",
            field=models.CharField(
                blank=True, max_length=200, verbose_name="Link Klassen (css)"
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="author",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Autor*in",
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="sections.Category",
                verbose_name="Kategorie",
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="created_date",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="Erstellungsdatum"
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="edited_date",
            field=models.DateTimeField(auto_now=True, verbose_name="Bearbeitungsdatum"),
        ),
        migrations.AlterField(
            model_name="event",
            name="end_date",
            field=models.DateTimeField(verbose_name="End-Datum"),
        ),
        migrations.AlterField(
            model_name="event",
            name="header_image",
            field=imagefield.fields.ImageField(
                blank=True,
                height_field="header_image_height",
                null=True,
                upload_to="",
                verbose_name="Header Bild",
                width_field="header_image_width",
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="location",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="events.Location",
                verbose_name="Ort",
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="namespace",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="events.NameSpace",
                verbose_name="Namensraum",
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="publication_date",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="Publikationsdatum"
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="section",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="sections.Section",
                verbose_name="Sektion",
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="start_date",
            field=models.DateTimeField(verbose_name="Start-Datum"),
        ),
        migrations.AlterField(
            model_name="event",
            name="template_key",
            field=models.CharField(
                choices=[("default", "Standard")],
                default="default",
                max_length=100,
                verbose_name="template",
            ),
        ),
        migrations.AlterField(
            model_name="eventplugin",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                related_query_name="+",
                to="sections.Category",
                verbose_name="Kategorie",
            ),
        ),
        migrations.AlterField(
            model_name="eventplugin",
            name="count",
            field=models.IntegerField(default=3, verbose_name="Anzahl"),
        ),
        migrations.AlterField(
            model_name="eventplugin",
            name="events",
            field=models.ManyToManyField(
                blank=True,
                related_name="_eventplugin_events_+",
                related_query_name="+",
                to="events.Event",
                verbose_name="Events",
            ),
        ),
        migrations.AlterField(
            model_name="eventplugin",
            name="namespace",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                related_query_name="+",
                to="events.NameSpace",
                verbose_name="Namensraum",
            ),
        ),
        migrations.AlterField(
            model_name="formplugin",
            name="form",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                related_query_name="+",
                to="forms.Form",
                verbose_name="Formular",
            ),
        ),
        migrations.AlterField(
            model_name="image",
            name="caption",
            field=models.CharField(blank=True, max_length=200, verbose_name="Titel"),
        ),
        migrations.AlterField(
            model_name="location",
            name="city",
            field=models.CharField(max_length=100, verbose_name="Ort"),
        ),
        migrations.AlterField(
            model_name="location",
            name="country",
            field=models.CharField(max_length=200, verbose_name="Land"),
        ),
        migrations.AlterField(
            model_name="location",
            name="header_image",
            field=imagefield.fields.ImageField(
                blank=True,
                height_field="header_image_height",
                null=True,
                upload_to="",
                verbose_name="Header Bild",
                width_field="header_image_width",
            ),
        ),
        migrations.AlterField(
            model_name="location",
            name="lat",
            field=models.FloatField(default=0, verbose_name="Latitude"),
        ),
        migrations.AlterField(
            model_name="location",
            name="lng",
            field=models.FloatField(default=0, verbose_name="Longitude"),
        ),
        migrations.AlterField(
            model_name="location",
            name="section",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="sections.Section",
                verbose_name="Sektion",
            ),
        ),
        migrations.AlterField(
            model_name="location",
            name="street",
            field=models.CharField(max_length=200, verbose_name="Strasse"),
        ),
        migrations.AlterField(
            model_name="location",
            name="website",
            field=models.URLField(blank=True, verbose_name="Website"),
        ),
        migrations.AlterField(
            model_name="location",
            name="zip_code",
            field=models.CharField(max_length=20, verbose_name="PLZ"),
        ),
        migrations.AlterField(
            model_name="locationimage",
            name="caption",
            field=models.CharField(blank=True, max_length=200, verbose_name="Titel"),
        ),
        migrations.AlterField(
            model_name="team",
            name="columns",
            field=models.CharField(
                choices=[("two", "2"), ("three", "3"), ("four", "4"), ("five", "5")],
                default="three",
                max_length=10,
                verbose_name="Spalten",
            ),
        ),
        migrations.AlterField(
            model_name="team",
            name="team",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="people.Team",
                verbose_name="Team",
            ),
        ),
    ]
