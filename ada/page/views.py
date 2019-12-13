from django.shortcuts import render
from products.models import Product, ProductImage

def page(request, page_id):
    product = Product.objects.get(id=page_id)
    return render(request, 'ada/page.html', locals())
