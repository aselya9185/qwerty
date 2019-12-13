from django.urls import path
from . import views

urlpatterns=[
    path('', views.players, name='players'),
    path('detail/<int:pk>', views.detail, name='details')
]