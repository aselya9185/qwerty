from django.urls import path,include
from registration import views
from registration import views as v
app_name = "registration"
urlpatterns = [
    path('',views.registr,name='Login'),

]