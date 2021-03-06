from django.db import models

from core.models import TimeStamp

class Product(TimeStamp):
    name           = models.CharField(max_length=200)
    category       = models.ForeignKey('Category', on_delete = models.CASCADE, related_name = 'product')
    theme          = models.ForeignKey('Theme', on_delete = models.CASCADE, related_name ='product')
    author         = models.ForeignKey('Author', on_delete = models.CASCADE, related_name = 'product')
    release_price  = models.DecimalField(max_digits = 15, decimal_places=2)
    model_number   = models.IntegerField()
    release_date   = models.DateTimeField()

    class Meta:
        db_table = 'products'

class ProductImage(models.Model):
    product    = models.ForeignKey('Product', on_delete = models.CASCADE)
    image_urls = models.URLField()
    
    class Meta:
        db_table = 'images'

class ProductSize(models.Model):
    size    = models.ForeignKey('Size', on_delete = models.CASCADE, related_name = 'products_sizes')
    product = models.ForeignKey('Product', on_delete = models.CASCADE, related_name = 'products_sizes')

    class Meta:
        db_table = 'products_size'

class Size(models.Model):
    name = models.CharField(max_length = 50)

    class Meta:
        db_table = 'sizes'

class Author(models.Model):
    name = models.CharField(max_length = 50)
    
    class Meta:
        db_table = 'authors'

class Wishlist(models.Model):
    product = models.ForeignKey('Product', on_delete = models.CASCADE, related_name = 'wishlist')
    user    = models.ForeignKey('users.User', on_delete = models.CASCADE, related_name = 'wishlist')
    size    = models.ForeignKey('Size', on_delete=models.CASCADE, related_name='wishlist')

    class Meta:
        db_table = 'wishlists'

class Theme(models.Model):
    name = models.CharField(max_length = 50)

    class Meta:
        db_table = 'themes'

class Category(models.Model):
    name = models.CharField(max_length = 50)
    
    class Meta:
        db_table  = 'categories'