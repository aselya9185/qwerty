import datetime
from datetime import datetime
from django.db import models

from django.utils import timezone

class ProductCategory(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "Product's category"
        verbose_name_plural = "Products categories"

class Product(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount = models.IntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    size = models.CharField(max_length=100, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Product %s" % self.name
        #это нужно для того чтобы когда в терминале вводишь команду Webexample.objects.all() выводило то что хранится в этой таблице
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='pictures/')
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Order %s" % self.id
        #это нужно для того чтобы когда в терминале вводишь команду Webexample.objects.all() выводило то что хранится в этой таблице
    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"