# Generated by Django 3.0.5 on 2020-07-23 17:50

from django.db import migrations
import feincms3.cleanse


class Migration(migrations.Migration):

    dependencies = [
        ("people", "0012_auto_20200523_1748"),
    ]

    operations = [
        migrations.AddField(
            model_name="person",
            name="bio",
            field=feincms3.cleanse.CleansedRichTextField(blank=True),
        ),
    ]