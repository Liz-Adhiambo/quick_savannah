from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    number=models.CharField(max_length=15,null=True, blank=True)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.DateTimeField(auto_now_add=True)