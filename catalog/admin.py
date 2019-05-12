from django.contrib import admin
from catalog.models import Category, Shop, Product, ProductImage


admin.site.register(Category)
admin.site.register(Shop)
admin.site.register(Product)
admin.site.register(ProductImage)
