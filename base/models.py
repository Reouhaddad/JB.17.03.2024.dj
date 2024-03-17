from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    user =models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')
    price = models.FloatField()
    description = models.CharField(max_length=100 ,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.title
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"

class OrderDetails(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order #{self.order.id} - {self.product.name}"