# Generated by Django 3.0.5 on 2020-05-29 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0020_auto_20200529_1523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form',
            name='generated_meta_image_height',
        ),
        migrations.RemoveField(
            model_name='form',
            name='generated_meta_image_ppoi',
        ),
        migrations.RemoveField(
            model_name='form',
            name='generated_meta_image_width',
        ),
        migrations.AlterField(
            model_name='form',
            name='generated_meta_image',
            field=models.ImageField(blank=True, null=True, upload_to='meta', verbose_name='generated meta image'),
        ),
    ]
