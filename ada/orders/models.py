from django.db import models
from products.models import Product
from django.db.models.signals import post_save

class Status(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Status %s" % self.name
        #это нужно для того чтобы когда в терминале вводишь команду Webexample.objects.all() выводило то что хранится в этой таблице
    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Statuses"

class Order(models.Model):
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0) #total price for all products in order
    customer_name = models.CharField(max_length=128, blank=True, null=True, default=None)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=50, blank=True, null=True, default=None)
    customer_address = models.CharField(max_length=128, blank=True, null=True, default=None)
    comments = models.TextField(blank=True, null=True, default=None)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Order %s %s" % (self.id, self.status.name)
        #это нужно для того чтобы когда в терминале вводишь команду Webexample.objects.all() выводило то что хранится в этой таблице
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, blank=True, null=True, default=None)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, blank=True, null=True, default=None)
    number = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0) #price*num
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Order %s" % self.product.name
        #это нужно для того чтобы когда в терминале вводишь команду Webexample.objects.all() выводило то что хранится в этой таблице

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def save(self, *args, **kwargs):
        price_per_item = self.product.price #price of product from Product model
        self.price_per_item = price_per_item
        self.total_price = self.number * self.price_per_item #counter * price of one item
        super(ProductInOrder, self).save(*args, **kwargs)

def Product_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_products_in_order = ProductInOrder.objects.filter(order=order, is_active=True)

    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += (item.total_price * 95)/100  # общая сумма

    instance.order.total_amount = order_total_price
    instance.order.save(force_update=True)  # чтобы сказать что нужно обновить запись, а не сделать новую
    
post_save.connect(Product_in_order_post_save, sender=ProductInOrder)

class Buyer(models.Model):
    name=models.CharField(max_length=50)
    surname=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    password2=models.CharField(max_length=50)
    def __str__(self):
        return "Buyer %s %s"  % (self.name , self.surname)