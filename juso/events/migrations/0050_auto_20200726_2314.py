# Generated by Django 3.0.5 on 2020-07-26 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0075_auto_20200726_2314"),
        ("events", "0049_event_author"),
    ]

    operations = [
        migrations.RemoveField(model_name="event", name="namespace",),
        migrations.RemoveField(model_name="eventplugin", name="namespace",),
        migrations.DeleteModel(name="NameSpace",),
    ]
