from django.contrib import admin
from Home.models import *


@admin.register(Product)
class ProductModel(admin.ModelAdmin):
    list_display =['id','product_name','product_category','product_quantity','product_status','product_price']
    
admin.site.register(ProductCategory)