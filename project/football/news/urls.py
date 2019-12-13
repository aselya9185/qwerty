from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='news'),
    path('news/<int:pk>/', views.detail, name='detail'),
]