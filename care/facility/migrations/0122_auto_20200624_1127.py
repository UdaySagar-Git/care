# Generated by Django 2.2.11 on 2020-06-24 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0121_auto_20200619_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalpatientregistration',
            name='allow_transfer',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='patientregistration',
            name='allow_transfer',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='patientsearch',
            name='allow_transfer',
            field=models.BooleanField(default=True),
        ),
    ]