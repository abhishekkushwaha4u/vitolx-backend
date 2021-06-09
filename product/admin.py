from django.contrib import admin
from product.models import (
    Product,
    ProductImage
)

admin.site.register(Product)
admin.site.register(ProductImage)