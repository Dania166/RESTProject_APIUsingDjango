from django.contrib import admin
from .models import Customer, Product, Order, Review


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'first_name', 'last_name')
    search_fields = ('customer_id', 'first_name', 'last_name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'product', 'quantity', 'created_at')
    search_fields = ('customer__first_name', 'customer__last_name', 'product__name')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('customer', 'product', 'rating', 'review')
    search_fields = ('customer__first_name', 'customer__last_name', 'product__name')