# Generated by Django 5.1.6 on 2025-02-25 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="slug",
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
