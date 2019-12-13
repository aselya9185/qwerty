from django.urls import path
from . import views

urlpatterns = [
    path('', views.productMen, name='mens'),
]