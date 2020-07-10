# Generated by Django 3.0.5 on 2020-07-01 07:32

import re

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        #        ('forms', '0026_auto_20200701_0932'),
        ("blog", "0040_auto_20200626_1201"),
    ]

    operations = [
        migrations.CreateModel(
            name="FormEntryCounterPlugin",
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
                (
                    "steps",
                    models.CharField(
                        default="50, 100, 500, 1000",
                        max_length=200,
                        validators=[
                            django.core.validators.RegexValidator(
                                re.compile("^\\d+(?:,\\d+)*\\Z"),
                                code="invalid",
                                message=None,
                            )
                        ],
                        verbose_name="steps",
                    ),
                ),
                ("start", models.IntegerField(default=0, verbose_name="start")),
                ("region", models.CharField(max_length=255)),
                ("ordering", models.IntegerField(default=0)),
                (
                    "form",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="blog_formentrycounterplugin",
                        to="forms.Form",
                        verbose_name="form",
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="blog_formentrycounterplugin_set",
                        to="blog.Article",
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
    ]