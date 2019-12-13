import smtplib

from django.views import generic
from .forms import RegisterForm
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .models import Bus, Client, DateGoingOut, Seats, Image
from django.core.mail import send_mail

class SignUp(generic.CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def home(request):
    return render(request,'page1.html')

def buses(request):
    bus_list=Bus.objects.all()
    date_list=DateGoingOut.objects.all()
    wanted_buses=[]
    wanted_dates=[]
    buses=[]
    dates=[]
    s=0
    ss=[]
    if 'from_name' and 'to_name' and 'dr' in request.GET:
        message1=request.GET['from_name']
        message2=request.GET['to_name']
        message3=request.GET['dr']
        for bus in bus_list:
            if message1 == bus.from_city and message2 == bus.to_city:
                wanted_buses.append(bus)
        for date in date_list:
            if message3==str(date):
                wanted_dates.append(date)
        for bus in wanted_buses:
            for date in wanted_dates:
                if bus.id==date.bus.id:
                    buses.append(bus)
                    dates.append(date)
                    s+=1
        #for i in wanted_dates:
        #     wanted_buses.append(Bus.objects.get(id=i.bus.id))
        return render(request, 'page2.html', {'buses': buses,'message1':message1,'message2':message2,'message3':message3,'quantity':s,'dates':dates})

    #return render(request,'mainpage/page1.html')
def seats(request,bus_id,date_id):
    date = DateGoingOut.objects.get(id=date_id)
    ddd = Seats.objects.filter(date=date)
    bus=Bus.objects.get(pk=bus_id)
    if not ddd:
        for i in range(0,43):
            ss=Seats(id=None,date=DateGoingOut.objects.get(pk=date_id),status=True,number=i+1)
            ss.save()
            ddd = Seats.objects.all()
    rrr=[]
    n=0
    for x in ddd:
        if x.status==True:
            rrr.append(x)
            n+=1
    return render(request, 'page3.html', {'ddd': rrr,'bus':bus,'date':date,'n':n})

def passengerinfo(request,bus_id,date_id):
    bus=Bus.objects.get(pk=bus_id)
    date=DateGoingOut.objects.get(pk=date_id)
    if 'seat_number_field' in request.POST:
        message1 = request.POST.get('seat_number_field')
        seat=Seats.objects.get(date=date,number=message1)
        seat.status=False
        seat.save(update_fields=['status'])
    return render(request, "page4.html",{'message1':message1,'bus':bus,'date':date})


def send_email(request,bus_id,date_id):
    if 'name' and 'email' and 'surname' and 'number' in request.POST:
        message1=request.POST.get('name')
        message2=request.POST.get('email')
        message3=request.POST.get('surname')
        message4=request.POST.get('number')
        message5=request.POST.get('card_number')
        a=Client(name=str(message1),surname=str(message3),email=str(message2),identity_card_number=str(message4),card_number=str(message5))
        a.save()
    bus=Bus.objects.get(pk=bus_id)
    date=DateGoingOut.objects.get(pk=date_id)

    return render(request,'page5.html',{'message1':message1,'message2':message2,'message3':message3,'message4':message4,'bus':bus,'date':date,'a':a})

def images(request):
    imgs=Image.objects.all()
    return render(request,'images.html',{'imgs':imgs})
