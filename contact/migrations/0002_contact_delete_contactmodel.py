# Generated by Django 5.0.2 on 2024-02-24 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contact", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("full_name", models.CharField()),
                ("email", models.EmailField(max_length=254)),
                ("subject", models.CharField()),
                ("message", models.CharField()),
            ],
        ),
        migrations.DeleteModel(
            name="ContactModel",
        ),
    ]
