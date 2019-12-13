from django.urls import path
from . import views

urlpatterns = [
    path("product/(?P<page_id>\w+)", views.page, name='page')
]