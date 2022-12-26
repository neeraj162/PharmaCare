from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):

    # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,blank=True)

    username = models.CharField(max_length=200,primary_key=True)
    firstname = models.CharField(max_length=200,null=True)
    lastname = models.CharField(max_length=200,null=True)

    password = models.CharField(max_length=200,null=True)

    phonecode = models.CharField(max_length=10,null=True)
    phNo = models.IntegerField(null=True)
    email = models.CharField(max_length=200,null=True)

    houseNo = models.CharField(max_length=200,null=True)
    area = models.CharField(max_length=200,null=True)
    state = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=200,null=True)
    pincode = models.IntegerField(null=True)
    requirement = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.username

    
    

class Medicines(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    mg = models.IntegerField()
    price  = models.FloatField(null=True)
    available = models.IntegerField(null=True)

    