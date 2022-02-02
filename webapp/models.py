from django.db import models



class Product(models.Model):
    product_id = models.CharField(max_length=20)
    product_name = models.CharField(max_length=20)
    product_image = models.ImageField(upload_to="static/img/upload")
    product_description = models.CharField(max_length=200)
    product_price = models.CharField(max_length=20)
    product_buyer = models.CharField(max_length=20)

class Cart(models.Model):
    Buyer_Name = models.CharField(max_length=20)
    Item_Name = models.CharField(max_length=20)
    Item_Quantity = models.CharField(max_length=20)
    Price = models.CharField(max_length=20)

class Contact(models.Model):
    Name = models.CharField(max_length=20)
    Email = models.CharField(max_length=20)
    Message = models.CharField(max_length=200)
# Create your models here.
