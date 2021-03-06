# Generated by Django 3.0.3 on 2020-02-15 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Membership",
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
                ("title", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Person",
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
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("email", models.EmailField(blank=True, max_length=254)),
                ("homepage", models.URLField(blank=True)),
            ],
            options={
                "verbose_name": "person",
                "verbose_name_plural": "people",
                "ordering": ["last_name", "first_name"],
            },
        ),
        migrations.CreateModel(
            name="Team",
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
                ("name", models.CharField(max_length=200)),
                (
                    "members",
                    models.ManyToManyField(
                        related_name="teams",
                        through="people.Membership",
                        to="people.Person",
                    ),
                ),
            ],
            options={"ordering": ["name"],},
        ),
    ]
