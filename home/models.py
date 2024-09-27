from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Products(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    product_image = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=18, decimal_places=2)
    stock = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name