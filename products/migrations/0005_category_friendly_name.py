# Generated by Django 5.0.2 on 2024-02-13 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='friendly_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
