# Generated by Django 4.2.10 on 2024-05-28 11:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0440_merge_20240528_1613"),
    ]

    operations = [
        migrations.AddField(
            model_name="patientnotes",
            name="reply_to",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="replies",
                to="facility.patientnotes",
            ),
        ),
    ]
