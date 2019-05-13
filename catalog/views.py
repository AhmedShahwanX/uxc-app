from rest_framework import generics

from .models import Category, Shop, Product, ProductImage
from .serializers import CategorySerializer, ShopSerializer, ProductSerializer, ProductImageSerializer


class CategoryList(generics.ListCreateAPIView):
    """
    get:
    Return a list of all the existing categories.

    post:
    Create a new category instance.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ShopList(generics.ListCreateAPIView):
    """
    get:
    Return a list of all shops.

    post:
    Create a new shop.
    """
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class ProductList(generics.ListCreateAPIView):
    """
    get:
    Return a list of all products.

    post:
    Create a new product.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductImages(generics.ListCreateAPIView):
    """
    get:
    Return a list of all products' images.

    post:
    Create a new product image.
    """
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
