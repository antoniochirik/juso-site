# Generated by Django 3.0.3 on 2020-03-02 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("people", "0006_auto_20200215_2346"),
    ]

    operations = [
        migrations.AddField(
            model_name="team",
            name="translations",
            field=models.ManyToManyField(
                related_name="_team_translations_+", to="people.Team"
            ),
        ),
    ]
