from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


def shop_directory_path(instance, filename):
    """Path to save shops profile pictures"""
    # MEDIA_ROOT/shop/<shop_id>/profile_picture
    return f"shop/{instance.id}/profile_picture"


def product_image_path(instance, filename):
    """Path to save product gallery images"""
    # MEDIA_ROOT/shop/<shop_id>/products/<filename>
    return f"shop/{instance.product.shop.id}/products/{filename}"


class Category(models.Model):
    name = models.CharField(max_length=50)


class Shop(models.Model):
    picture = models.ImageField(upload_to=shop_directory_path, height_field=200, width_field=200, max_length=255)
    categories = models.ManyToManyField(Category, related_name="shops")
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = PhoneNumberField()
    website = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)


class Product(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    size = models.CharField(max_length=2)
    brand = models.CharField(max_length=50)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="gallery")
    image = models.ImageField(upload_to=None, max_length=255)
