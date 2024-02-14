# Generated by Django 5.0.2 on 2024-02-13 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_brand_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='product',
            name='in_stock',
        ),
        migrations.RemoveField(
            model_name='product',
            name='on_sale',
        ),
        migrations.RemoveField(
            model_name='product',
            name='sale_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='stock_amount',
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='static/'),
        ),
    ]