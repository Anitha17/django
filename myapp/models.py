from django.db import models

# Create your models here.
class Userdata(models.Model):
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.email
class Product(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='products/')
    dcost=models.IntegerField()
    cost=models.IntegerField()
    desc=models.TextField()

    def __str__(self):
        return self.name

class Cart(models.Model):
    user=models.ForeignKey(Userdata,on_delete=models.CASCADE)
    item=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.user 

class Bill(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zip=models.IntegerField()
    paymentMethod=models.CharField(max_length=100)