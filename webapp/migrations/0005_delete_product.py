# Generated by Django 4.0 on 2022-01-25 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_alter_product_product_description'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
    ]
