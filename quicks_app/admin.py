from django.contrib import admin
from . models import *

# Register your models here.
@admin.register(Customer)
class Customer(admin.ModelAdmin):
    list_display = ("name", "code")
    list_per_page = 20


@admin.register(Order)
class Order(admin.ModelAdmin):
    list_display = ("item", "amount")
    list_per_page = 20