from rest_framework import generics

from .models import Category, Shop, Product, ProductImage
from .serializers import CategorySerializer, ShopSerializer, ProductSerializer, ProductImageSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ShopList(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductImages(generics.ListCreateAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
