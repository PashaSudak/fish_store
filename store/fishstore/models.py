from distutils.command.upload import upload
from email.policy import default
from tokenize import group
from django.db import models
from datetime import date
from django.contrib.auth.models import User

class Product (models.Model):
    freshfish = 'freshfish'
    frozenfish = 'frozenfish'
    fishfillet = 'fishfillet'
    cannedfish = 'cannedfish'

    CHOICE_GROUP = {
        (freshfish, 'freshfish'),
        (frozenfish, 'frozenfish'),
        (fishfillet, 'fishfillet'),
        (cannedfish, 'cannedfish')
    }

    name = models.CharField(max_length=50)
    group = models.CharField(max_length=20, choices = CHOICE_GROUP, default = freshfish)
    description = models.TextField()
    price = models.IntegerField()
    availability = models.BooleanField(default = True)
    img = models.ImageField(default = 'no_image.png', upload_to = 'product_image')
    dateAdded = models.DateField(default = date.today())

    def __str__(self):
        return f'{self.name}'
    

class Customer (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    fullname = models.CharField(max_length=100)
    # adress = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
        
    def __str__(self):
        return f'{self.username} , {self.email} , {self.phone}'


class Order (models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    complete = models.BooleanField(default=False, null=True, blank=False)

    def __str__(self):
        return f'{self.id}'

    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total() for item in orderitems])
        return total

    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem (models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)

    def get_total(self):
        total = self.product.price * self.quantity
        return total
