# Generated by Django 5.0.2 on 2024-02-19 23:13

import django.db.models.deletion
import django_countries.fields
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('default_phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('default_street_address1', models.CharField(blank=True, max_length=80, null=True)),
                ('default_street_address2', models.CharField(blank=True, max_length=80, null=True)),
                ('default_town_or_city', models.CharField(blank=True, max_length=40, null=True)),
                ('default_county', models.CharField(blank=True, max_length=80, null=True)),
                ('default_postcode', models.CharField(blank=True, max_length=20, null=True)),
                ('default_country', django_countries.fields.CountryField(blank=True, max_length=40, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]