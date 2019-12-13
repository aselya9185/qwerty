from django.urls import path
from . import views

urlpatterns = [
    path('', views.productChild, name='child'),
]