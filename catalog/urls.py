from django.urls import path, re_path
from .views import CategoryList, ShopList, ProductList, ProductImages


urlpatterns = [
    path('category/', CategoryList.as_view(), name="category"),
    path('shop/', ShopList.as_view(), name="shop"),
    path('product/', ProductList.as_view(), name="product"),
    path('product_gallery', ProductImages.as_view(), name="product_images"),
    # path('^$', viewset) # docs
]
