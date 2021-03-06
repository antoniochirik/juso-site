# Generated by Django 3.0.5 on 2020-05-05 18:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("sections", "0007_auto_20200502_2048"),
    ]

    operations = [
        migrations.CreateModel(
            name="Collection",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=120, verbose_name="Name")),
                (
                    "section",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sections.Section",
                        verbose_name="section",
                    ),
                ),
            ],
            options={
                "verbose_name": "collection",
                "verbose_name_plural": "collections",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Link",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.CharField(max_length=120, verbose_name="Text")),
                ("target", models.URLField(verbose_name="Ziel")),
                ("order", models.IntegerField(default=0)),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="sections.Category",
                        verbose_name="category",
                    ),
                ),
                (
                    "collection",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="link_collections.Collection",
                        verbose_name="Collection",
                    ),
                ),
            ],
            options={
                "verbose_name": "link",
                "verbose_name_plural": "links",
                "ordering": ["order"],
            },
        ),
    ]
