# Generated by Django 4.1.1 on 2022-11-08 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomBookStore', '0009_customer_order_customerid'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='productImage',
            field=models.ImageField(blank=True, upload_to='product_images'),
        ),
    ]
