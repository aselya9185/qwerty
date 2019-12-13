from django.urls import path,include
from sales import views

app_name = "sales"
urlpatterns = [
    path('',views.sales,name='sales'),

]