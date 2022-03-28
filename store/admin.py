from django.contrib import admin
from .models.product import Products
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']

class AdminCustomer(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','email','phone','password']
    
    
class AdminOrder(admin.ModelAdmin):
    list_display = ['id','customer','quantity','price','address','phone','status']
# Register your models here.
admin.site.register(Products,AdminProduct)
admin.site.register(Category)
admin.site.register(Customer,AdminCustomer)
admin.site.register(Order,AdminOrder)


# username = Tanushree, email = tanushree7252@gmail.com, password = 1234
