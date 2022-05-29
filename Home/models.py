from django.db import models


class ProductCategory(models.Model):
    category_name = models.CharField(max_length=50)
    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length=250)
    product_quantity = models.IntegerField()
    product_stock_availability = models.IntegerField()
    product_description = models.TextField()
    product_price = models.IntegerField()
    product_images =  models.ImageField(upload_to='media/product-images/')
    product_status = models.BooleanField(default=False)
    product_category = models.ForeignKey(ProductCategory,on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.product_name  