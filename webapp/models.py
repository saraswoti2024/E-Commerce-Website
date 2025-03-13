from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Category(models.Model):
    catitle = models.CharField(max_length=255)
    def __str__(self):
        return self.catitle

class Product(models.Model):
    title=models.CharField(max_length=255)
    brand_name = models.TextField()
    # desc = models.TextField()
    Category1 = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    price=models.DecimalField(max_digits=10,decimal_places=2,null=True)
    image=models.ImageField(upload_to="images") 

    def __str__(self):
        return self.title

class Users(models.Model):
    email = models.EmailField(null=True,unique=True)
    number = PhoneNumberField(null=True,region='NP')
    messages = models.TextField(null=True)
    address = models.TextField(null=True)
