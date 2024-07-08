# Generated by Django 5.0.2 on 2024-07-08 13:02

import django_countries.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="default_country",
            field=django_countries.fields.CountryField(
                blank=True, max_length=2, null=True
            ),
        ),
    ]