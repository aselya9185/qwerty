from django.urls import path,include
from login import views
from registration import views as v
app_name = "login"
urlpatterns = [
    path('', views.login,name='Registration'),
]