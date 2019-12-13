from django.shortcuts import render
from ada.forms import BuyerForm

def registr(request):
    form = BuyerForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        new_form = form.save()
    return render(request, 'ada/login.html', locals())








