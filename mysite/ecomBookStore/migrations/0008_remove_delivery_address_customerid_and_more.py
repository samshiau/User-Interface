# Generated by Django 4.1.1 on 2022-11-01 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecomBookStore', '0007_delete_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivery_address',
            name='customerID',
        ),
        migrations.RemoveField(
            model_name='payment_method',
            name='customerID',
        ),
        migrations.RemoveField(
            model_name='customer_order',
            name='customerID',
        ),
        migrations.DeleteModel(
            name='customer',
        ),
        migrations.DeleteModel(
            name='delivery_address',
        ),
        migrations.DeleteModel(
            name='payment_method',
        ),
    ]
