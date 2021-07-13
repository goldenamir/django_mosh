from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)

class Customer(models.Model):
    MEMBERSHIP_CHOICE = [
        ('B', 'Bronze'),
        ('S','Silver'),
        ('G','Gold')
    ]


    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateTimeField(null = True)
    membership = models.charField(max_length=1, choices = MEMBERSHIP_CHOICE, default='B')

class Order(models.Model):
    place_at = models.DateTimeField(auto_now_add=True)

    PAYMENT_STATUS = [
        ('P','Pending'),
        ('C','Complete'),
        ('F','Failed')
    ]

    payment = models.charField(max_length = 1, choice = PAYMENT_STATUS, default = 'P')
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

# Creating one to one realtionship 
'''
Assumption: every customer should have only one address and each 
address should goes to one customer.
'''
class Address(models.Model):
    street = models.CharField(max_length= 255)
    city = models.CharField(max_length=255)
    # customer is parent of Address (i.e., address is child of customer)
    # if we delete customer the related address should be deleted
    # customer = models.oneToOneField(Customer, on_delete=models.CASCADE,primary_key=True)


    # if we want to have several addresses for a customer
    # in this case, we do NOT need primary key here, since
    # we plan to duplicate the several addresses
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

# adding one to many reltion for collection and product
class Collection(models.Model):  
    title = models.CharField(max_length= 255)
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.models.PositiveSmallInteger()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    quantity = models.models.PositiveSmallIntegerField()