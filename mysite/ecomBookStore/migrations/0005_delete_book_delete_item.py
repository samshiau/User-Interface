# Generated by Django 4.1.1 on 2022-10-25 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecomBookStore', '0004_book'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
