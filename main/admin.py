from django.contrib import admin
from . import models

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price')

admin.site.register(models.Product, ProductAdmin)
@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'price', 'image')
