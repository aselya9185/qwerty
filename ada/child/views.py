from django.shortcuts import render
from products.models import Product, ProductImage

def productChild(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_women = products_images.filter(product__category__id=1)
    products_images_men = products_images.filter(product__category__id=2)
    products_images_child = products_images.filter(product__category__id=5)
    return render(request, 'ada/prod_child.html', locals())
