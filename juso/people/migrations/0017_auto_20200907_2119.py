# Generated by Django 3.1 on 2020-09-07 19:19

from django.db import migrations
import imagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ("people", "0016_auto_20200821_1354"),
    ]

    operations = [
        migrations.AlterField(
            model_name="candidature",
            name="image",
            field=imagefield.fields.ImageField(
                blank=True,
                height_field="image_height",
                help_text="Only necessary if you want to use another picture for this candidature.",
                null=True,
                upload_to="people/",
                verbose_name="image",
                width_field="image_width",
            ),
        ),
        migrations.AlterField(
            model_name="membership",
            name="image",
            field=imagefield.fields.ImageField(
                blank=True,
                height_field="image_height",
                help_text="Only necessary if you want to use another picture for this position.",
                null=True,
                upload_to="people/",
                verbose_name="image",
                width_field="image_width",
            ),
        ),
    ]
