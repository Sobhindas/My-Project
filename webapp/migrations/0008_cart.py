# Generated by Django 4.0 on 2022-01-30 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_alter_product_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Buyer_Name', models.CharField(max_length=20)),
                ('Item_Name', models.CharField(max_length=20)),
                ('Item_Quantity', models.CharField(max_length=20)),
                ('Price', models.CharField(max_length=20)),
            ],
        ),
    ]
