from django.shortcuts import render
from ada.forms import BuyerForm

def sales(request):
    return render(request, 'ada/sales.html', locals())








