from django.urls import path
from django.urls import path
from django.contrib.auth.views import auth_login
from . import views
from django.views.generic import ListView,DetailView
from mainpage.models import Bus
from . import views


app_name='mainpage'
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('images/',views.images,name='images'),
    path('buses/',views.buses,name='buses'),
    path('buses/<int:bus_id>/seats/<int:date_id>',views.seats,name='seats'),
    path('buses/<int:bus_id>/seats/<int:date_id>/passengerinfo/',views.passengerinfo,name='passengerinfo'),
    path('buses/<int:bus_id>/seats/<int:date_id>/passengerinfo/send_email/',views.send_email,name='send_email'),
]

