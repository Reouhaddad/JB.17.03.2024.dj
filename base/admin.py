from django.contrib import admin
from .models import Category,Order,OrderDetails,Product

# Register your models here.
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderDetails)
admin.site.register(Product)
