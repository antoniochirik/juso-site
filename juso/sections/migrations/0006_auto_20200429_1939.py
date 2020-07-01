# Generated by Django 3.0.3 on 2020-04-29 17:39

import imagefield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sections", "0005_category_color"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="header_image",
            field=imagefield.fields.ImageField(
                blank=True,
                height_field="header_image_height",
                null=True,
                upload_to="",
                verbose_name="header image",
                width_field="header_image_width",
            ),
        ),
        migrations.AddField(
            model_name="category",
            name="header_image_height",
            field=models.PositiveIntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name="category",
            name="header_image_ppoi",
            field=imagefield.fields.PPOIField(default="0.5x0.5", max_length=20),
        ),
        migrations.AddField(
            model_name="category",
            name="header_image_width",
            field=models.PositiveIntegerField(blank=True, editable=False, null=True),
        ),
    ]
