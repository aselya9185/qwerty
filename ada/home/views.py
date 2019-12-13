from django.shortcuts import render


def mainpage(request):
    #form=UserForm(request.POST or None)
    #if request.method == 'POST' and form.is_valid():
        #print(request.POST)
        #print(form.cleaned_data)

        #new_form= form.save()

    return render(request,'ada/homepage.html',locals())
